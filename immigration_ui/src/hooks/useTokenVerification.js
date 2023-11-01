import { useSelector } from "react-redux"
import validator from "./tokenValidation"

export function useTokenVerification() {

    const appUser = useSelector((state) => {
        return state["app-user"]
    })

    const token = appUser && appUser['token']
    const isVerified = validator(token)

    if (!isVerified) {

        window.localStorage.removeItem('persist:root')
        window.location.href = '/'
    }

    return isVerified
}