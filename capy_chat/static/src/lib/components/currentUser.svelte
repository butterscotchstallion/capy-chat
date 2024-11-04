<script lang="ts">
    async function getUserInfo() {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/user");
            if (response.ok) {
                const responseJSON = await response.json();
                
            } else {
                console.log("API response error");
                return null;
            }
        } catch (error) {
            console.log("Error getting user info: " + error);
            return null;
        }
    }
</script>
