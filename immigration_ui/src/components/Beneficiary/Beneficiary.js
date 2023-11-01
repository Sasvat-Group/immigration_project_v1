import React, { useEffect, useState } from 'react'
import { Card, Col, Nav, Row, Tab } from 'react-bootstrap'
import { v4 as uuidv4 } from 'uuid'
import './beneficiary.style.scss'
import PageHeader from 'layouts/PageHeader/PageHeader'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { beneficiaryService } from 'services/beneficiary.service'
import { actions } from 'store/slices/beneficiarySlice'
import { SimpleLoader } from 'components/Common/SimpleLoader'

const importLazyTabs = (component) => {
    return React.lazy(() => import('./TabComponents').then((module) => ({ default: module[component] })))
}

const BeneficiaryImmigrationTimeline = importLazyTabs('BeneficiaryImmigrationTimeline')
const ImmigrationStatusKeyDates = importLazyTabs('ImmigrationStatusKeyDates')
const OpenCases = importLazyTabs('OpenCases')
const WorkAuthorizationInfo = importLazyTabs('WorkAuthorizationInfo')
const BeneficiaryQuickAssessmentForm = importLazyTabs('BeneficiaryQuickAssessmentForm')
const PRProcessInitiationInfo = importLazyTabs('PRProcessInitiationInfo')
const EmploymentInfo = importLazyTabs('EmploymentInfo')
const PassportTravel = importLazyTabs('PassportTravel')
const PersonalData = importLazyTabs('PersonalData')
const PriorityData = importLazyTabs('PriorityData')
const DMSWorkspaceLink = importLazyTabs('DMSWorkspaceLink')

export default function BeneficiaryInfo() {
    const navigate = useNavigate()
    const [searchParams, _] = useSearchParams()
    const dispatch = useDispatch()

    const _currentBeneficiary = useSelector((state) => state.beneficiary.profileData.beneficiary)
    const appUser = useSelector((state) => state['app-user'])

    const [tabs, setTabs] = useState([
        {
            id: 1,
            title: 'Beneficiary Immigration Timeline',
            component: <BeneficiaryImmigrationTimeline />,
            active: false
        },
        {
            id: 2,
            title: 'Beneficiary Quick Assessment Form',
            component: <BeneficiaryQuickAssessmentForm />,
            active: false
        },
        {
            id: 3,
            title: 'Immigration Status & Key Dates',
            component: <ImmigrationStatusKeyDates />,
            active: false
        },
        {
            id: 4,
            title: 'Projects',
            component: <OpenCases />,
            active: false
        },
        {
            id: 5,
            title: 'Work Authorization Info',
            component: <WorkAuthorizationInfo />,
            active: false
        },
        {
            id: 6,
            title: 'PR Process Info',
            component: <PRProcessInitiationInfo />,
            active: false
        },
        {
            id: 7,
            title: 'Priority Info',
            component: <PriorityData />,
            active: false
        },
        {
            id: 8,
            title: 'Employment Info',
            component: <EmploymentInfo />,
            active: false
        },
        {
            id: 9,
            title: 'Passport & Travel',
            component: <PassportTravel />,
            active: false
        },
        {
            id: 10,
            title: 'Personal Info',
            component: <PersonalData />,
            active: false
        },
        {
            id: 11,
            title: 'DMS Workspace Link',
            component: <DMSWorkspaceLink />,
            active: false
        }
    ])

    const handleTabClick = (index) => {
        if (index === 10) {
            window.open(
                `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`,
                '_blank'
            )
            return null
        }

        let nTabs = tabs.map((tab) => {
            tab.active = false
            return tab
        })

        nTabs[index].active = true

        navigate({
            pathname: './',
            search: '?pane=' + (index + 1)
        })

        setTabs(nTabs)
    }

    const TabComponent = () => {
        return (
            <Tab.Content className="tab-content">
                <React.Suspense fallback={<SimpleLoader />}>
                    {tabs.map((tab, index) => {
                        return (
                            <Tab.Pane key={uuidv4()} eventKey={index} active={tab.active === true}>
                                {tab.active === true ? tab.component : <h2>not active</h2>}
                            </Tab.Pane>
                        )
                    })}
                </React.Suspense>
            </Tab.Content>
        )
    }

    const loadAPI = () => {
        dispatch(actions.setTabLoader({ tab: 'beneficiary', status: true }))
        beneficiaryService.getBeneficiaryList().then((res) => {
            dispatch(actions.setBeneficiaryList(res))
        })
    }

    useEffect(() => {
        if (appUser.usertype === 'Beneficiary')
            dispatch(actions.setBeneficiary({ name: `${appUser.firstname} ${appUser.lastname}`, id: appUser.id }))
        else loadAPI()
    }, [])

    const TabPlaceholder = () => {
        if (_currentBeneficiary.id == 0) return <EmptyComponent message={'Please select a beneficiary'} />
        else if (searchParams.size && searchParams.get('pane')) return <TabComponent />
        else return <EmptyComponent message={'Please select an item from the tab.'} />
    }

    const EmptyComponent = ({ message }) => {
        return (
            <div className="p-3 mt-5 text-center text-bold">
                <i className="mdi mdi-alert-octagon h1"></i>
                <h5>{message}</h5>
            </div>
        )
    }

    const BeneficiaryContent = () => {
        return (
            <div className="beneficiary-info-container">
                <Row className="row-sm">
                    <Col lg={12}>
                        <Card className="mb-3">
                            <Card.Body className="p-1">
                                <Tab.Container id="left-tabs-example" defaultActiveKey="first">
                                    <Row>
                                        <Col className="tab-partition-left">
                                            <Nav variant="pills" className="flex-column m-2">
                                                {tabs.map((tab, index) => {
                                                    return (
                                                        <Nav.Item key={uuidv4()}>
                                                            <Nav.Link
                                                                active={tab.active === true}
                                                                onClick={() => handleTabClick(index)}
                                                                eventKey={index}
                                                            >
                                                                {tab.title}
                                                            </Nav.Link>
                                                        </Nav.Item>
                                                    )
                                                })}
                                            </Nav>
                                        </Col>
                                        <Col className="tab-partition-right">
                                            <TabPlaceholder />
                                        </Col>
                                    </Row>
                                </Tab.Container>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        )
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader
                Header="Beneficiary Information"
                BreadcrumbItemList={[{ name: 'Beneficiary Info' }, { name: _currentBeneficiary.name }]}
            />

            <BeneficiaryContent />
        </React.Fragment>
    )
}
