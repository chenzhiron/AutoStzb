import Vue from 'vue'

import App from './App'
if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.prototype.$message = ElementUI.Message
/* eslint-disable no-new */
new Vue({
  components: { App },
  template: '<App/>'
}).$mount('#app')
