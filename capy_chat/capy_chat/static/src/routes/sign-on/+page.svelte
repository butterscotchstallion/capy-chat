<script>
	import SignInWindow from './signInWindow.svelte';
	export let form;
</script>

<main>
	<div class="grid auto-cols-max grid-flow-col">
		{#if form?.error}
			<p class="error">{form.error}</p>
		{/if}
		<SignInWindow />
	</div>
</main>
