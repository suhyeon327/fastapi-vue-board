/// <reference types="vite/client" />

declare module '*.vue' {
    import { DefineComponent, resolveComponent } from 'vue'
    const component: DefineComponent<{}, {}, any>
    export default component
}