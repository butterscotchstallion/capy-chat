import { fail } from "@sveltejs/kit";

export const actions = {
	default: async ({ request }) => {
		const data = await request.formData();
		const username = data.get("username");
		const password = data.get("password");

		// TODO: validate creds here
		if (!username || !password) {
			return fail(422, {
				description: "Username and password are required.",
				error: "Missing required fields"
			})
		}
	}
};