import React, { Fragment, useEffect } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Route, Routes, useLocation, useNavigate } from 'react-router-dom'
import 'index.scss'
import Loader from 'layouts/Loader/Loader'
import Auth from 'Authentication/auth'
import CaseInfo from 'components/CaseInfo/CaseInfo'
import CostSpecData from 'components/CaseInfo/CaseSpecData'
import CaseOverview from 'components/CaseInfo/CaseOverview'
import CaseProcess from 'components/CaseInfo/CaseProcess'
import BeneficiaryInfo from 'components/Beneficiary/Beneficiary'
import Petitioner from 'components/PetitionerInfo/Petitioner'
import Document from 'components/Documents/documents'
import Marketplace from 'components/Marketplace/Marketplace'
import PERMCases from 'components/PERMInfo/PERMCases'
import PERMOverall from 'components/PERMInfo/PERMOverall'
import PERMInfo from 'components/PERMInfo/PERMInfo'
import QuickLinks from 'components/QuickLinks/QuickLinks'
import Integration from 'components/Integrations/Integrations'
import ImmigrationToolkit from 'components/ImmigrationToolkit/ImmigrationToolkit'
import Reports from 'components/Reports/Reports'
import ComplianceInfo from 'components/ComplianceInfo/ComplianceInfo'
import Temp from 'components/Temp'
import Profile from 'components/Profile/Profile'
import { Provider } from 'react-redux'
import { store } from 'store/store'
import { PersistGate } from 'redux-persist/integration/react'
import { persistStore } from 'redux-persist'
import { useTokenVerification } from 'hooks/useTokenVerification'

const Dashboard = React.lazy(() => import('./components/Dashboard/Dashboard'))
const App = React.lazy(() => import('components/app'))

const Error404 = React.lazy(() => import('./components/CustomPages/Error1-404/Error-404.js'))
const AuthLogin = React.lazy(() => import('Authentication/Login'))
const AuthSignup = React.lazy(() => import('Authentication/Signup'))

let persistor = persistStore(store)

const AuthGauard = ({ component }) => {
    const isTokenVerified = useTokenVerification()

    const location = useLocation()
    const navigate = useNavigate()

    useEffect(() => {
        // if (!isTokenVerified)
        //     return navigate('/', { state: { tokenFailed: true } })
    }, [location.pathname])

    if (isTokenVerified) return component
    else return null
}

const Root = () => {
    return (
        <Fragment>
            <Provider store={store}>
                <PersistGate persistor={persistor}>
                    <BrowserRouter>
                        <React.Suspense fallback={<Loader />}>
                            <Routes>
                                <Route path={`${process.env.PUBLIC_URL}/`} element={<Auth />}>
                                    <Route index element={<AuthLogin />} />
                                    <Route
                                        path={`${process.env.PUBLIC_URL}/authentication/login`}
                                        element={<AuthLogin />}
                                    />
                                    <Route
                                        path={`${process.env.PUBLIC_URL}/authentication/signup`}
                                        element={<AuthSignup />}
                                    />
                                </Route>
                                <Route path={`${process.env.PUBLIC_URL}/`} element={<AuthGauard component={<App />} />}>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/dashboard/`} element={<Dashboard />} />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/temp`} element={<Temp />} />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/documents/`} element={<Document />} />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/integrations/`}
                                            element={<Integration />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/petitioner-info`}
                                            element={<Petitioner />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/case-info`} element={<CaseInfo />} />
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/case-info/overview`}
                                            element={<CaseOverview />}
                                        />
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/case-info/process`}
                                            element={<CaseProcess />}
                                        />
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/case-info/specific`}
                                            element={<CostSpecData />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/PERM-info`} element={<PERMInfo />} />
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/PERM-info/cases`}
                                            element={<PERMCases />}
                                        />
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/PERM-info/overall`}
                                            element={<PERMOverall />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/beneficiary`}
                                            element={<BeneficiaryInfo />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/marketplace`}
                                            element={<Marketplace />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/quick-links/`}
                                            element={<QuickLinks />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/reports/`} element={<Reports />} />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/toolkit/`}
                                            element={<ImmigrationToolkit />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route
                                            path={`${process.env.PUBLIC_URL}/compliance-info/`}
                                            element={<ComplianceInfo />}
                                        />
                                    </Route>
                                    <Route>
                                        <Route path={`${process.env.PUBLIC_URL}/profile/`} element={<Profile />} />
                                    </Route>
                                </Route>

                                {/* <Route path={`${process.env.PUBLIC_URL}/landingpage`} element={<Landingpageapp />} /> */}
                                {/* ........................................Errorpage............................................... */}
                                <Route path="*" element={<Error404 />} />
                            </Routes>
                        </React.Suspense>
                    </BrowserRouter>
                </PersistGate>
            </Provider>
        </Fragment>
    )
}
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<Root />)
