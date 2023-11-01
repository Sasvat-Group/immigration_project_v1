import axios from 'axios'
import { Zoom, toast } from 'react-toastify'

const isProd = process.env.NODE_ENV === 'development' ? false : true

const api = axios.create({
    withCredentials: false,
    baseURL: isProd ? 'http://20.228.144.215:7000/' : 'http://localhost:7000/'
})

console.log('--p', isProd)
// baseURL: "http://20.228.144.215:7000/",

const ErrorComp = ({ statusCode, message }) => {
    return (
        <p className="mx-2 tx-16 d-flex flex-column align-items-start mb-0">
            {statusCode ? (
                <div>
                    <b>Status: {statusCode}</b>
                </div>
            ) : null}
            {message}
        </p>
    )
}

const errorHandler = (error) => {
    let statusCode = null
    let message = null

    if (error.code === 'ERR_NETWORK') {
        // console.error(error)
        message = 'Network Error'
    } else if (error.response?.status) {
        statusCode = error.response?.status

        if (statusCode && statusCode === 401) {
            window.localStorage.removeItem('persist:root')

            if (window.location.pathname !== '/') window.location.href = '/'
        } else {
            // console.error(error)
        }

        if (error.response && error?.response?.data?.Error) message = error?.response?.data?.Error
    }

    if (error?.config.url !== '/signin')
        toast.error(<ErrorComp statusCode={statusCode} message={message} />, {
            position: toast.POSITION.TOP_CENTER,
            transition: Zoom,
            autoClose: false
        })

    return Promise.reject(error)
}

api.interceptors.request.use((config) => {
    const root = JSON.parse(localStorage.getItem('persist:root'))
    const appUser = JSON.parse(root?.['app-user'] || '{}')

    if (appUser && appUser.token) {
        config.headers.Authorization = `Bearer ${appUser.token}`
    }
    return config
})

api.interceptors.response.use(undefined, (error) => {
    return errorHandler(error)
})

export { api }
