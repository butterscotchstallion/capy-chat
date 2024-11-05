Signed in as {userInfo.username}

<script lang="ts">
    function getCookie(name: string): string | undefined {
        return document.cookie
            .split("; ")
            .find((row) => row.startsWith(name + "="))
            ?.split("=")[1];
    }

    async function getUserInfo() {
        let user = null;
        try {
            const sessionID: string | undefined = getCookie("sessionID");
            if (sessionID) {
                const response = await fetch("http://127.0.0.1:8000/api/session/" + sessionID);
                if (response.ok) {
                    console.log("Got session info");
                    const responseJSON = await response.json();
                    console.log(responseJSON);

                    user = responseJSON["user"];
                } else {
                    console.log("API response error");
                }
            } else {
                console.log("No sessionID cookie");
            }
            return user;
        } catch (error) {
            console.log("Error getting user info: " + error);
            return null;
        }
    }

    let userInfo = getUserInfo();
</script>
