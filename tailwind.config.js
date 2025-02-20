/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./templates/**/*.html",  // ✅ Include Django templates
        "./cms_app/templates/**/*.html",  // ✅ Include app-specific templates
        "./cms_app/static/**/*.js",  // ✅ Include JS files
    ],
    darkMode: 'class',
    theme: {
        extend: {},
    },
    plugins: [],
}