<script>
	import '../../node_modules/98.css/style.css';
</script>

<svelte:head>
	<title>Capy Chat</title>
</svelte:head>

<slot />

<style lang="scss">
	@import '$lib/scss/_variables';
	:global(body) {
		background-color: $background-color;
	}
</style>
