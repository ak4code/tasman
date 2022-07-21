import ElementPlus from 'element-plus'
import locale  from 'element-plus/lib/locale/lang/ru'
import '@/assets/element-variables.scss'

export default (app) => {
  app.use(ElementPlus, { locale })
}
