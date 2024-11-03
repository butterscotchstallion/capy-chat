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

            const {status, message, session_id} = await response.json();

            if (status === "OK" && session_id) {
                cookies.set("sessionID", session_id, {
                    path: "/",
                    httpOnly: true,
                    sameSite: 'lax'
                });
                throw redirect(303, "/dashboard")
            } else {
                return fail(401, {
                    description: message,
                    error: status
                });
            }
        } else {
            return fail(422, {
                description: "Username and password are required.",
                error: "Missing required fields"
            })
        }
    }
};
