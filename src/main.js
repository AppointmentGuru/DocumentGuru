// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import 'element-ui/lib/theme-default/index.css'

Vue.config.productionTip = false

// Element components:

import {
  Upload,
  Button
} from 'element-ui'

Vue.component(Upload.name, Upload)
Vue.use(Button)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
