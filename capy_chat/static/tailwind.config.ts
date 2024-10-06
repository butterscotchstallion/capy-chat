import type { Config } from 'tailwindcss';

export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		fontSize: {
			'2xl': ['1.5rem', {
				lineHeight: '2rem',
				letterSpacing: '-0.01em',
				fontWeight: '500',
			}],
			'3xl': ['1.875rem', {
				lineHeight: '2.25rem',
				letterSpacing: '-0.02em',
				fontWeight: '700',
			}],
		}
	},

	plugins: [require('@tailwindcss/typography')]
} as Config;
