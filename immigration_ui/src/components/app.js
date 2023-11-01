import React, { Fragment, useEffect } from 'react'

import Header from 'layouts/Header/Header'
import Sidebar from 'layouts/SideBar/SideBar'
import Footer from 'layouts/Footer/Footer'
import { Outlet, useNavigate } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import { useSelector } from 'react-redux'
import tokenValidation from 'hooks/tokenValidation'
import { useTokenVerification } from 'hooks/useTokenVerification'
import Loader from 'layouts/Loader/Loader'

const App = () => {
    /* ------------------------------- Conditions ------------------------------- */

    document.querySelector('body').classList.remove('error-1')
    document.querySelector('body').classList.remove('app', 'sidebar-mini', 'landing-page', 'horizontalmenu')
    document.querySelector('body').classList.add('main-body', 'leftmenu')

    /* -------------------------------- functions ------------------------------- */

    useTokenVerification()

    const appUser = useSelector((state) => {
        return state['app-user']
    })

    const remove = () => {
        document.querySelector('body').classList.remove('main-sidebar-show')
    }

    /* -------------------------------- useEffects ------------------------------- */

    useEffect(() => {
        if (appUser['usertype'] === 'Beneficiary') {
            window.ChatGen && window.ChatGen.init({ widget_key: 'mtia3lI4' })
        } else if (appUser['usertype'] === 'Attorney' || appUser['usertype'] === 'Paralegal') {
            window.ChatGen && window.ChatGen.init({ widget_key: '8oukOW6s' })
        }
    }, [])

    /* --------------------------------- Render --------------------------------- */

    return (
        <Fragment>
            <div className="horizontalMenucontainer">
                <div className="page">
                    <Header />
                    <Sidebar />
                    <div className="main-content side-content">
                        <div className="main-container container-fluid" onClick={() => remove()}>
                            <div className="inner-body">
                                <Outlet />
                            </div>
                        </div>
                    </div>
                </div>
                <Footer />
                <ToastContainer />
            </div>
        </Fragment>
    )
}
export default App
