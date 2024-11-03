<script>
    import SignInWindow from './signInWindow.svelte';

    export let form;
</script>

<main>
    {#if form?.error}
        <h4 class="text-2xl">Error signing on</h4>
        <p class="error">{form.error}</p>
    {/if}

    <div class="grid auto-cols-max grid-flow-col">
        <SignInWindow/>
    </div>
</main>
