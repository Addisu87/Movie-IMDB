/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');
const colors = require('tailwindcss/colors');

module.exports = {
	mode: 'jit',
	darkMode: 'class', //false, class, media
	content: [
		'./core/templates/**/*.html', // Adjust content path to include all templates
		'./static/**/*.css',
		'./static/**/*.js',
	],
	theme: {
		screens: {
			xs: '350px',
			...defaultTheme.screens,
		},
		extend: {
			colors: {
				transparent: 'transparent',
				current: 'currentColor',
				black: colors.black,
				white: colors.white,
				gray: colors.neutral,
				red: colors.red,
				yellow: colors.amber,
				green: colors.emerald,
				blue: colors.blue,
				indigo: colors.indigo,
				purple: colors.purple,
				pink: colors.pink,
			},
			fontFamily: {
				montserrat: ['Montserrat', 'sans-serif'],
				poppins: ['Poppins', 'sans-serif'],
			},
			fontSize: {
				xxs: '.65rem',
			},
		},
	},
	plugins: [],
};
