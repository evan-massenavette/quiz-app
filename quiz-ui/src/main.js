import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import '@mdi/font/css/materialdesignicons.css'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

const darkTheme = {
  dark: true,
  variables: {}, // To avoid crash because of bug from Vuetify
  colors: {
    background: '#212121',
    surface: '#303134',
    primary: '#03a9f4',
    secondary: '#9c27b0',
    accent: '#2196f3',
    error: '#f44336',
    warning: '#ffc107',
    info: '#607d8b',
    success: '#4caf50',
  }
}

// TODO: Make light theme colors
const lightTheme = darkTheme

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'darkTheme',
    variations: {
      colors: ['background', 'surface', 'primary', 'secondary', 'accent'],
      lighten: 5,
      darken: 5,
    },
    themes: {
      darkTheme,
      lightTheme,
    }
  }
})

const app = createApp(App)

app.use(router)
app.use(vuetify)

export default createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    }
  },
})

app.mount('#app')