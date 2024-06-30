/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
	mode: 'jit',
	darkMode: 'class', //false, class, media
	content: [
		'./core/templates/core/*.html',
		'./static/**/*.css',
		'./static/**/*.js',
	],
	theme: {
		screens: {
			xs: '350px',
			...defaultTheme.screens,
		},
		extend: {
			colors: {},
			fontFamily: {
				montserrat: ['Montserrat', 'sans-serif'],
				poppins: ['Poppins', 'sans-serif'],
			},
			fontSize: {
				xxs: '.65rem',
			},
		},
	},
	plugins: [require('@tailwindcss/aspect-ratio')],
};
