import React from 'react'
import { Card, Col, ListGroup, Row } from 'react-bootstrap'
import StepZilla from "react-stepzilla"
import { v4 as uuidv4 } from 'uuid'
import { Fragment } from 'react'
import { Link } from 'react-router-dom'
import { useSelector } from 'react-redux'
import PageHeader from 'layouts/PageHeader/PageHeader'

const Test = () => {
    return (
        <Fragment>
            <div>
                <section className="pt-3">
                    {/* <h5>Test 0</h5> */}
                </section>
            </div>
        </Fragment>
    )
}

const stepswizard = [
    { name: 'Initiation', component: <Test /> },
    { name: 'Information/Document\nCollection', component: <Test /> },
    { name: 'In Drafting', component: <Test /> },
    { name: 'Docs under Review/Signature', component: <Test /> },
    { name: 'Project Filed & Pending', component: <Test /> },
    { name: 'Decision Recived', component: <Test /> }
]

const AccordionWizardForm = () => {
    return (
        <div className='step-progress'>
            <StepZilla steps={stepswizard} showNavigation={false} />
        </div>
    )
}

const getComponent = ({ value, type }) => {

    if (type === 'link') {
        return <Link to={value}>View</Link>
    }

    return <span>{value}</span>
}

export default function CaseProcess() {

    const checkTypeAttorney = () => localStorage.getItem('user_type') === "attorney" ? true : false

    const caseProcessStore = useSelector((state) => {
        return state['case-process']
    })


    const data = [{
        name: 'Global Supporting Documents', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGlobal%20Supporting%20Docs&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Project Specific Supporting Documents', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FProject%20Specific%20Supporting%20Docs&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Government Filings', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Filings&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Government Notices', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Notices&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'PERM Docs', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FPERM%20Docs&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Correspondence', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FCorrespondence&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Misc.', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FMisc&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }, {
        name: 'Project ID and Project Name: 2883-I-485 Application', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2F2883%2DI%2D485%20Application&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
    }]

    const handleLink = (link) => {
        window.open(link, '_blank')
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Project Process" BreadcrumbItemList={[{ name: 'Project Info', link: '/case-info/' }, { name: "Project Process" }]} />

            <div className='case-process-container'>
                <Row className="row row-sm static-cards">
                    <Col lg={4}>
                        <Card className="custom-card">
                            <Card.Body className="">
                                <div className='text-center'>
                                    <div className="icon-service bg-info-transparent rounded-circle text-info">
                                        <i className="fe fe-trending-up"></i>
                                    </div>
                                    <div className="mt-2">
                                        <h5 className="mb-1">Key Link</h5>
                                    </div>
                                </div>
                                <ListGroup className="projects-list mt-3" >
                                    {data.map((item, index) => {
                                        return <ListGroup.Item action
                                            className="flex-column align-items-start p-2"
                                            key={index}
                                        >
                                            <div onClick={() => handleLink(item.link)} className="d-flex w-100 justify-content-between">
                                                <h6 className="mb-1 font-weight-semibold ">{item.name}</h6>
                                            </div>
                                        </ListGroup.Item>
                                    })}
                                </ListGroup>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col lg={4}>
                        <Card className="custom-card">
                            <Card.Body className="text-center">
                                <div className="icon-service bg-secondary-transparent rounded-circle text-secondary">
                                    <i className="fe fe-git-pull-request"></i>
                                </div>
                                <div className="mt-2">
                                    <h5 className="mb-1">Project First Review Sheet</h5>
                                    <p className="mb-0 text-muted">
                                        From Info/Docs Requested to Project Filing
                                    </p>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col lg={4}>
                        <Card className="custom-card case-drafting-card">
                            <Card.Body className="text-center">
                                <div className="d-flex align-items-center">
                                    <div className="icon-service bg-primary-transparent rounded-circle text-primary">
                                        <i className="fe fe-arrow-down"></i>
                                    </div>
                                    <div className="d-flex flex-column mx-2">
                                        <h5 className="mb-1">Project Drafting</h5>
                                        <div className='d-flex align-items-left'>
                                            <input type='checkbox' className='mx-2' /> Manual
                                            <input type='checkbox' className='mx-2' /> RPA
                                        </div>
                                    </div>
                                </div>
                                <ul className="task-list">
                                    <li>
                                        <i className="task-icon bg-primary"></i>
                                        <ListGroup className="task-list-group" >
                                            {caseProcessStore.caseDrafting.drafting.steps.map(step => {
                                                return <ListGroup.Item action
                                                    className="flex-column align-items-start p-2"
                                                    key={uuidv4()}
                                                >
                                                    <div className="d-flex w-100 justify-content-between">
                                                        <h6 className="font-weight-semibold ">{step.name}</h6>
                                                        {getComponent(step)}
                                                    </div>
                                                </ListGroup.Item>
                                            })}
                                        </ListGroup>
                                    </li>
                                    <li>
                                        <i className="task-icon bg-secondary"></i>
                                        <ListGroup className="task-list-group mt-3" >
                                            {caseProcessStore.caseDrafting.reDrafting.steps.map(step => {
                                                return <ListGroup.Item action
                                                    className="flex-column align-items-start p-2"
                                                    key={uuidv4()}
                                                >
                                                    <div className="d-flex w-100 justify-content-between">
                                                        <h6 className="font-weight-semibold ">{step.name}</h6>
                                                        {getComponent(step)}
                                                    </div>
                                                </ListGroup.Item>
                                            })}
                                        </ListGroup>
                                    </li>
                                </ul>

                            </Card.Body>
                        </Card>
                    </Col>
                </Row>

                <Row>
                    <Col xl={12} className="col-xl-6 mx-auto">
                        <Card className="custom-card">
                            <Card.Body className="">
                                <label className="main-content-label my-auto pt-2">
                                    Project Milestone
                                </label>
                                <div className="checkout-steps wrapper">
                                    <div id="checkoutsteps">
                                        <AccordionWizardForm />
                                    </div>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        </React.Fragment>
    )
}

