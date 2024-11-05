import {fail, redirect} from "@sveltejs/kit";

export const actions = {
    "sign-on": async ({request, cookies}) => {
        const data: FormData = await request.formData();
        const username: FormDataEntryValue | null = data.get("username");
        const password: FormDataEntryValue | null = data.get("password");

        if (username && password) {
            const response: Response = await fetch("http://127.0.0.1:8000/user/sign-on", {
                method: "POST",
                body: JSON.stringify({
                    username,
                    password
                }),
                headers: {
                    "Content-Type": "application/json"
                }
            });

            console.log("Retrieved sign on info");

            const {status, details} = await response.json();

            if (status === "OK" && details.session_id) {
                cookies.set("sessionID", details.session_id, {
                    path: "/",
                    httpOnly: false,
                    sameSite: 'lax'
                });
                console.log("Set session ID and redirecting....");
                throw redirect(303, "/dashboard")
            } else {
                console.log("Unable to obtain session: " + status + ": " + details.message);
                return fail(401, {
                    description: details.message,
                    error: details.message
                });
            }
        } else {
            console.log("No username/password provided.");
            return fail(422, {
                description: "Username and password are required.",
                message: "Missing required fields"
            })
        }
    }
};
