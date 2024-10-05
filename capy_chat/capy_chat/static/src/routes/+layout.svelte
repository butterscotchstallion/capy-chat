<script>
	import '../../node_modules/xp.css/dist/XP.css';
	import '../app.css';
	import TailwindCss from '../lib/tailwind.svelte';
</script>

<TailwindCss />

<svelte:head>
	<title>Capy Chat</title>
</svelte:head>

<div class="md:container md:mx-auto">
	<div class="grid auto-cols-max grid-flow-col">
		<div class="flex">
			<slot class="justify-center" />
		</div>
	</div>
</div>

<style>
	:global(body) {
		background-color: #008080;
	}
</style>
