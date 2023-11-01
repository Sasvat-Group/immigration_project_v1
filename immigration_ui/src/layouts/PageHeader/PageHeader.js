import React, { Fragment } from "react"
import { Breadcrumb, BreadcrumbItem, Button, Col, Form, Modal, Row } from "react-bootstrap"
import { setBeneficiarySearchModal } from 'store/slices/commonSlice'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from "react-router-dom"
import BasicSearch from "components/Search/BasicSearch"
import { useState } from "react"
import Multiselect from "react-select"

const PageHeader = ({ Header, BreadcrumbItemList }) => {

    const navigate = useNavigate()
    const dispatch = useDispatch()

    const appUser = useSelector((state) => {
        return state['app-user']
    })


    const [petitioner, setShow1] = useState(false)
    const [beneficiary, setShow2] = useState(false)
    const [createCase, setShow3] = useState(false)
    const objectArray = [
        { value: "Firefox", label: "firefox" },
        { value: "Chrome", label: "chrome " },
        { value: "Safari", label: "safari" },
        { value: "Operate", label: "operate" },
        { value: " Internet Explore", label: "internet explore " },
    ]

    let viewDemoShow = (modal) => {
        //  [eslint]
        switch (modal) {
            case "petitioner":
                setShow1(true)
                break
            case "beneficiary":
                setShow2(true)
                break
            case "createCase":
                setShow3(true)
                break
            default:
            // do nothing
        }
    }

    let viewDemoClose = (modal) => {
        switch (modal) {
            case "petitioner":
                setShow1(false)
                break
            case "beneficiary":
                setShow2(false)
                break
            case "createCase":
                setShow3(false)
                break
            default:
            // do nothing
        }
    }
    return (
        <Fragment>
            <div className="page-header">
                <div>
                    <h2 className="main-content-title tx-24 mg-b-5">
                        {Header}
                    </h2>
                    <Breadcrumb>
                        <BreadcrumbItem onClick={() => navigate('/dashboard/')}>Home</BreadcrumbItem>
                        {BreadcrumbItemList.map((item, index) => (
                            <BreadcrumbItem key={index} onClick={() => navigate(item.link)}>{item.name}</BreadcrumbItem>
                        ))}
                    </Breadcrumb>
                </div>
                <div className="d-flex">
                    <div className="d-flex align-items-center">
                        <Button variant="white" type="button" className="me-3" onClick={() => viewDemoShow("petitioner")}><i className="fe fe-plus me-2"></i> Petitioner</Button>
                        {appUser?.usertype !== 'Beneficiary' ? <Button variant="white" type="button" className="me-3" onClick={() => viewDemoShow("beneficiary")}><i className="fe fe-user-plus me-2"></i> Beneficiary</Button> : null}
                        <Button variant="white" type="button" className="me-3" onClick={() => viewDemoShow("createCase")}><i className="fe fe-file-plus me-2"></i> Project</Button>
                        <Button
                            variant="primary"
                            type="button"
                            className="btn-icon-text"
                            onClick={() => dispatch(setBeneficiarySearchModal(true))}
                        >
                            <i className="fe fe-search me-2"></i> Search
                        </Button>
                    </div>
                </div>
            </div>
            <BasicSearch></BasicSearch>

            <Fragment>
                <Modal show={petitioner} size="md" backdrop="false">
                    <Modal.Header closeButton onClick={() => { viewDemoClose("petitioner") }}>
                        <Modal.Title>
                            <h6 className="main-content-label mb-1">Create Petitioner</h6>
                            <p className="text-muted card-sub-title mb-0">
                                All the fields are mandatory to create petitioner
                            </p>
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Row className="row-sm">
                            <Col md={12} lg={12} xl={12} >
                                <div className="">
                                    <div className="form-group">
                                        <label className="">Petitioner Name</label>
                                        <input className="form-control" required="" type="text" />
                                    </div>
                                    <p className="text-muted card-sub-title">
                                        Contact Person Details
                                    </p>
                                    <div className="form-group">
                                        <label className="">First Name</label>
                                        <input className="form-control" required="" type="text" />
                                    </div>
                                    <div className="form-group">
                                        <label className="">Last Name</label>
                                        <input className="form-control" required="" type="text" />
                                    </div>
                                    <div className="form-group">
                                        <label className="">Email</label>
                                        <div className="pos-relative">
                                            <input
                                                className="form-control"
                                                required=""
                                                type="email"
                                            />
                                        </div>
                                    </div>
                                    <div className="form-group mb-2 mt-4">
                                        <label className="ckbox">
                                            <input defaultdefaultchecked="true" type="checkbox" />
                                            <span className="tx-13">
                                                Send Questionnaire
                                            </span>
                                        </label>
                                    </div>
                                </div>
                            </Col>
                        </Row>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary"><i className="ti-pencil-alt me-2"></i>Create</Button>
                        <Button variant="secondary" onClick={() => { viewDemoClose("petitioner") }}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
            </Fragment>

            <Fragment>
                <Modal show={beneficiary} size="md" backdrop="false">
                    <Modal.Header closeButton onClick={() => { viewDemoClose("beneficiary") }}>
                        <Modal.Title>
                            <h6 className="main-content-label mb-1">Create Beneficiary</h6>
                            <p className="text-muted card-sub-title mb-0">
                                All the fields are mandatory to create beneficiary
                            </p>
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Row className="row-sm">
                            <Col md={12} lg={12} xl={12} >
                                <div className="">
                                    <p className="text-muted card-sub-title">
                                        Beneficiary Details
                                    </p>
                                    <div className="form-group">
                                        <label className="">First Name</label>
                                        <input className="form-control" required="" type="text" />
                                    </div>
                                    <div className="form-group">
                                        <label className="">Last Name</label>
                                        <input className="form-control" required="" type="text" />
                                    </div>
                                    <div className="form-group">
                                        <label className="">Email</label>
                                        <div className="pos-relative">
                                            <input className="form-control" required="" type="email" />
                                        </div>
                                    </div>
                                    <div className="form-group">
                                        <label className="">Petitioner Name</label>
                                        <Multiselect classNamePrefix="Select2" options={objectArray} singleSelect displayValue="key" />
                                    </div>
                                    <div className="form-group mb-2 mt-4">
                                        <label className="ckbox">
                                            <input defaultdefaultchecked="true" type="checkbox" />
                                            <span className="tx-13">
                                                Send Questionnaire
                                            </span>
                                        </label>
                                    </div>
                                </div>
                            </Col>
                        </Row>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary"><i className="ti-pencil-alt me-2"></i>Create</Button>
                        <Button variant="secondary" onClick={() => { viewDemoClose("beneficiary") }}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
            </Fragment>

            <Fragment>
                <Modal show={createCase} size="lg" backdrop="false">
                    <Modal.Header closeButton onClick={() => { viewDemoClose("createCase") }}>
                        <Modal.Title>
                            <h6 className="main-content-label mb-1">Create Project</h6>
                            <p className="text-muted card-sub-title mb-0">
                                All the fields are mandatory to create Project
                            </p>
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Row className="row-sm">
                            <Col md={12} lg={12} xl={12} >
                                <Row className="row-sm mg-b-20">
                                    <Col lg={6} className="">
                                        <div className="form-group">
                                            <label className="">Petitioner Name</label>
                                            <Multiselect classNamePrefix="petitioner" options={objectArray} singleSelect displayValue="key" />
                                        </div>
                                    </Col>
                                    <Col lg={6} className=" mg-t-20 mg-lg-t-0">
                                        <div className="form-group">
                                            <label className="">Beneficiary Name</label>
                                            <Multiselect classNamePrefix="beneficiary" options={objectArray} singleSelect displayValue="key" />
                                        </div>
                                    </Col>
                                </Row>
                                <Row className="row-sm mg-b-20">
                                    <Col lg={12} className="">
                                        <Row>
                                            <label className="">Project Type</label>
                                            <Col lg={4}><Form.Check defaultChecked name="rdio" type="radio" label="Type1" /></Col>
                                            <Col lg={4}><Form.Check defaultChecked name="rdio" type="radio" label="Type2" /></Col>
                                            <Col lg={4}><Form.Check defaultChecked name="rdio" type="radio" label="Type3" /></Col>
                                        </Row>
                                    </Col>
                                </Row>
                                <Row className="row-sm mg-b-20">
                                    <Col lg={4} className="">
                                        <div className="form-group">
                                            <label className="">Attorney-1 (Primary)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                    <Col lg={4} className=" mg-t-20 mg-lg-t-0">
                                        <div className="form-group">
                                            <label className="">Attorney-2 (Secondary)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                    <Col lg={4} className=" mg-t-20 mg-lg-t-0">
                                        <div className="form-group">
                                            <label className="">Attorney-3 (Additional)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                </Row>
                                <Row className="row-sm mg-b-20">
                                    <Col lg={4} className="">
                                        <div className="form-group">
                                            <label className="">Legal Staff-1 (Primary)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                    <Col lg={4} className="">
                                        <div className="form-group">
                                            <label className="">Legal Staff-2 (Secondary)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                    <Col lg={4} className="">
                                        <div className="form-group">
                                            <label className="">Legal Staff-3 (Additional)</label>
                                            <input className="form-control" required="" type="text" />
                                        </div>
                                    </Col>
                                </Row>
                                <div className="form-group mb-2 mt-4">
                                    <label className="ckbox">
                                        <input defaultdefaultchecked="true" type="checkbox" />
                                        <span className="tx-13">
                                            Send Questionnaire
                                        </span>
                                    </label>
                                </div>
                            </Col>
                        </Row>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary"><i className="ti-pencil-alt me-2"></i>Create</Button>
                        <Button variant="secondary" onClick={() => { viewDemoClose("createCase") }}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
            </Fragment>
        </Fragment>
    )
}

export default PageHeader
