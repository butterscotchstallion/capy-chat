const production = !process.env.ROLLUP_WATCH;
export default {
    plugins: [],
    theme: {
        extend: {},
    },
    purge: {
        content: [
            "./src/**/*.svelte",

        ],
        enabled: production // disable purge in dev
    },
    variants: {
        extend: {},
    },
    darkmode: true, // or 'media' or 'class'
    future: {
        purgeLayersByDefault: true,
        removeDeprecatedGapUtilities: true,
    },
}