import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark: false,
        themes: {
            dark: {
                primary: "#1969BB",
                // secondary: "#FFFFFD",
                // accent: "693D2A",
                opposite: "#FFFFFF",
                background: "#272727",
            },
            light: {
                primary: "#1969BB",
                secondary: "#212121",
                // accent: colors.blueGrey.base,
                opposite: "#000000",
                background: "#FFFFFF"
            }
        }
    }
});
