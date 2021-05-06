import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark: false,
        themes: {
            dark: {
                // primary: "#FF7028",
                // secondary: "#FFFFFD",
                // accent: "693D2A",
                opposite: "#FFFFFF",
                background: "#272727",
            },
            light: {
                // primary: "#5D0F2F",
                secondary: "#212121",
                // accent: colors.blueGrey.base,
                opposite: "#000000",
                background: "#FFFFFF"
            }
        }
    }
});
