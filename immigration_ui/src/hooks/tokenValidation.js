import jwtDecode from "jwt-decode"

const tokenValidation = (token) => {

    if (token && typeof token === 'string') {

        const _token = jwtDecode(token)

        if (_token !== null && _token !== undefined && typeof _token === 'object' && Date.now() < _token.exp * 1000)
            return true
    }
    return false
}

export default tokenValidation