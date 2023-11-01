import React, { Fragment, useState } from 'react'
import { Button, Card, Col, Modal, Row, Tab, Tabs } from 'react-bootstrap'
import PageHeader from 'layouts/PageHeader/PageHeader'

export default function Marketplace() {

    const [Basic, setShow1] = useState(false)

    let viewDemoShow = (modal) => {
        //  [eslint]
        switch (modal) {
            case "Basic":
                setShow1(true)
                break
            default:
                break
        }
    }

    let viewDemoClose = (modal) => {
        switch (modal) {
            case "Basic":
                setShow1(false)
                break
            default:
                break
        }
    }


    const ProviderTile = ({ data }) => {

        if (data) {
            return <Card className="card-aside custom-card">
                <img alt='media11'
                    src={require("../../assets/img/files/file.png")}
                    className="card-aside-column  cover-image rounded-start-11"
                />
                <Card.Body>
                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                        Provider Name
                    </h5>
                    <div className="">
                        Excepteur sint occaecat cupidatat non proident.
                    </div>
                    <div className="d-flex align-items-center pt-3 mt-auto">
                        <div className="media-icon bg-primary-transparent text-primary">
                            <i className="fe fe-user"></i>
                        </div>
                        <div className='ms-3'>
                            {/* <Card.Link href="#" className="text-default">
                        Contact
                    </Card.Link> */}
                            <small className="d-block text-muted">+21 3454 768 521</small>
                        </div>
                        <div className="ms-auto pt-1 text-muted">
                            <Button variant="outline-primary mt-1">View</Button>
                        </div>
                    </div>
                </Card.Body>
            </Card>
        } else
            return <Card className="card-aside custom-card">
                <img alt='media11'
                    src={require("../../assets/img/files/file.png")}
                    className="card-aside-column  cover-image rounded-start-11"
                />
                <Card.Body>
                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                        Provider Name
                    </h5>
                    <div className="">
                        Excepteur sint occaecat cupidatat non proident.
                    </div>
                    <div className="d-flex align-items-center pt-3 mt-auto">
                        <div className="media-icon bg-primary-transparent text-primary">
                            <i className="fe fe-user"></i>
                        </div>
                        <div className='ms-3'>
                            {/* <Card.Link href="#" className="text-default">
                            Contact
                        </Card.Link> */}
                            <small className="d-block text-muted">+21 3454 768 521</small>
                        </div>
                        <div className="ms-auto pt-1 text-muted">
                            <Button variant="outline-primary mt-1">View</Button>
                        </div>
                    </div>
                </Card.Body>
            </Card>
    }

    const ProviderSimpleTile = ({ providerName, username, email, contact, link }) => {

        if (providerName) {
            return <Card className="custom-card">
                <Card.Body>
                    <div className="card-block">
                        <div className="row align-items-center justify-content-center">
                            <div className="col-auto user-lock">
                                <div className='avatar avatar-xl d-none d-sm-flex bg-primary'>P</div>
                            </div>
                            <div className="col-8">
                                <h5>{providerName}</h5>
                                <div className="d-flex align-items-center pt-1 mt-auto">
                                    <div className='flex-1'>
                                        {/* <Card.Link href="#" className="text-default">
                                        Contact
                                    </Card.Link> */}
                                        <small className="d-block text-muted">{username}</small>
                                        <small className="d-block text-muted me-3">{contact}</small>
                                        <small className="d-block text-muted">{email}</small>
                                    </div>
                                    <div className="ms-auto text-muted">
                                        <Button variant="outline-primary mb-3" size="sm" onClick={() => window.open(link, '_blank')}>Website</Button>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </Card.Body>
            </Card>
        } else
            return <Card className="custom-card">
                <Card.Body>
                    <div className="card-block">
                        <div className="row align-items-center justify-content-center">
                            <div className="col-auto user-lock">
                                <div className='avatar avatar-xl d-none d-sm-flex bg-primary'>P</div>
                            </div>
                            <div className="col-8">
                                <h5>Provider Name</h5>
                                <div className="d-flex align-items-center pt-1 mt-auto">
                                    <div className='flex-1'>
                                        {/* <Card.Link href="#" className="text-default">
                                        Contact
                                    </Card.Link> */}
                                        <small className="d-block text-muted">Test Name</small>
                                        <small className="d-block text-muted me-3">+21 3454 768 521</small>
                                        <small className="d-block text-muted">test.user@gmail.com</small>
                                    </div>
                                    <div className="ms-auto text-muted">
                                        <Button variant="outline-primary mb-3" size="sm" onClick={() => viewDemoShow("Basic")}>Website</Button>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                </Card.Body>
            </Card>
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Marketplace" BreadcrumbItemList={[{ name: 'Marketplace' }]} />

            <div className='marketplace-container'>
                <div className='d-none'>
                    <Row className="row-sm">
                        <Col md={6}>
                            <h3 className='bg-primary shadow-1-strong'>Translation & Credential Services</h3>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                            </Row>
                        </Col>
                        <Col md={6}>
                            <h4>ALSP (Alternate Legal Service Provider)</h4>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}>
                                    <Card className="custom-card">
                                        <Card.Header className="p-2 tx-medium my-auto tx-white bg-light">
                                            Full Services
                                        </Card.Header>
                                        <Card.Body>
                                            <Row>
                                                <Col sm={6} className="border-end">
                                                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                                                        Provider Name
                                                    </h5>
                                                    <div className="">
                                                        Description
                                                    </div>
                                                    <div className="d-flex align-items-center pt-3 mt-auto">
                                                        <div className='ms-2'>
                                                            <Card.Link href="#" className="text-default">
                                                                Contact
                                                            </Card.Link>
                                                            <small className="d-block text-muted">+21 345 768</small>
                                                        </div>
                                                        <div className="ms-auto pt-1 text-muted">
                                                            <Button variant="outline-primary btn-sm">View</Button>
                                                        </div>
                                                    </div>
                                                </Col>
                                                <Col sm={6}>
                                                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                                                        Provider Name
                                                    </h5>
                                                    <div className="">
                                                        Description
                                                    </div>
                                                    <div className="d-flex align-items-center pt-3 mt-auto">
                                                        <div className='ms-2'>
                                                            <Card.Link href="#" className="text-default">
                                                                Contact
                                                            </Card.Link>
                                                            <small className="d-block text-muted">+21 345 768</small>
                                                        </div>
                                                        <div className="ms-auto pt-1 text-muted">
                                                            <Button variant="outline-primary btn-sm">View</Button>
                                                        </div>
                                                    </div>
                                                </Col>
                                            </Row>
                                        </Card.Body>
                                    </Card>
                                </Col>
                                <Col md={6} lg={6}>
                                    <Card className="custom-card">
                                        <Card.Header className="p-2 tx-medium my-auto tx-white bg-light">
                                            PERM Projects
                                        </Card.Header>
                                        <Card.Body>
                                            <Row>
                                                <Col sm={6} className="border-end">
                                                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                                                        Provider Name
                                                    </h5>
                                                    <div className="">
                                                        Description
                                                    </div>
                                                    <div className="d-flex align-items-center pt-3 mt-auto">
                                                        <div className='ms-2'>
                                                            <Card.Link href="#" className="text-default">
                                                                Contact
                                                            </Card.Link>
                                                            <small className="d-block text-muted">+21 345 768</small>
                                                        </div>
                                                        <div className="ms-auto pt-1 text-muted">
                                                            <Button variant="outline-primary btn-sm">View</Button>
                                                        </div>
                                                    </div>
                                                </Col>
                                                <Col sm={6}>
                                                    <h5 className="main-content-label tx-dark tx-medium mg-b-10">
                                                        Provider Name
                                                    </h5>
                                                    <div className="">
                                                        Description
                                                    </div>
                                                    <div className="d-flex align-items-center pt-3 mt-auto">
                                                        <div className='ms-2'>
                                                            <Card.Link href="#" className="text-default">
                                                                Contact
                                                            </Card.Link>
                                                            <small className="d-block text-muted">+21 345 768</small>
                                                        </div>
                                                        <div className="ms-auto pt-1 text-muted">
                                                            <Button variant="outline-primary btn-sm">View</Button>
                                                        </div>
                                                    </div>
                                                </Col>
                                            </Row>
                                        </Card.Body>
                                    </Card>
                                </Col>
                            </Row>
                        </Col>
                    </Row>
                    <Row className="row-sm mt-5">
                        <Col md={6}>
                            <h4>Operations Management Consultants</h4>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                            </Row>
                        </Col>

                        <Col md={6}>
                            <h4>PERM Ad Agencies</h4>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                            </Row>
                        </Col>
                    </Row>
                    <Row className="row-sm mt-5">
                        <Col md={6}>
                            <h4>Global Immigration Service Provider</h4>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                            </Row>
                        </Col>

                        <Col md={6}>
                            <h4>Relocation Companies</h4>
                            <Row className='mt-3'>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                                <Col md={6} lg={6}><ProviderTile /></Col>
                            </Row>
                        </Col>
                    </Row>
                </div>
                <div className=''>
                    <Row className='row-sm'>
                        <Col lg={6}>
                            <div>
                                <h4 className='text-primary shadow-1-strong px-1 d-table'>Translation & Credential Services</h4>
                            </div>
                            <Row className='mt-3'>
                                <Col md={6}><ProviderSimpleTile /></Col>
                                <Col md={6}><ProviderSimpleTile /></Col>
                            </Row>
                        </Col>
                        <Col md={6}>
                            <h4 className='text-secondary shadow-1-strong px-1 d-table'>ALSP (Alternate Legal Service Provider)</h4>
                            <Tabs
                                defaultActiveKey="Full Services"
                                className="nav panel-tabs main-nav-line"
                                style={{ justifyContent: 'right', marginTop: '-45px' }}
                            >
                                <Tab className='px-0' eventKey="Full Services" title="Full Services">
                                    <Row>
                                        <Col sm={6}>
                                            <ProviderSimpleTile />
                                        </Col>
                                        <Col sm={6}>
                                            <ProviderSimpleTile />
                                        </Col>
                                    </Row>
                                </Tab>
                                <Tab className='px-0' eventKey="PERM Cases" title="PERM Projects">
                                    <Row>
                                        <Col sm={6}>
                                            <ProviderSimpleTile />
                                        </Col>
                                        <Col sm={6}>
                                            <ProviderSimpleTile />
                                        </Col>
                                    </Row>
                                </Tab>
                            </Tabs>
                        </Col>
                    </Row>
                    <Row className='row-sm mt-4'>
                        <Col lg={6}>
                            <h4 className='text-primary shadow-1-strong px-1 d-table'>Operations Management Consultants</h4>
                            <Row className='mt-3'>
                                <Col md={6}><ProviderSimpleTile /></Col>
                                <Col md={6}><ProviderSimpleTile /></Col>
                            </Row>
                        </Col>
                        <Col lg={6}>
                            <h4 className='text-secondary shadow-1-strong px-1 d-table'>PERM Ad Agencies</h4>
                            <Row className='mt-3'>
                                <Col md={6}><ProviderSimpleTile
                                    providerName="Recruiter Networks (Recruiter Media Corporation)"
                                    username="Rochard Alman"
                                    email="Richard@recuirternetworks.com"
                                    contact="305-793-8225"
                                    link="http://www.recruiternetworks.com" /></Col>
                                <Col md={6}><ProviderSimpleTile /></Col>
                            </Row>
                        </Col>
                    </Row>
                    <Row className='row-sm mt-4'>
                        <Col lg={6}>
                            <h4 className='text-primary shadow-1-strong px-1 d-table'>Global Immigration Service Providers</h4>
                            <Row className='mt-3'>
                                <Col md={6}><ProviderSimpleTile
                                    providerName="Global Mobility Partners, LLC"
                                    username="Kyle Homstol"
                                    email="jyle@globalmobilitypartnersllc.com"
                                    contact="678-207-8436"
                                    link="http://www.globalmobilitypartnersllc.com" /></Col>
                                <Col md={6}><ProviderSimpleTile /></Col>
                            </Row>
                        </Col>
                        <Col lg={6}>
                            <h4 className='text-secondary shadow-1-strong px-1 d-table'>Relocation Providers</h4>
                            <Row className='mt-3'>
                                <Col md={6}><ProviderSimpleTile /></Col>
                                <Col md={6}><ProviderSimpleTile /></Col>
                            </Row>
                        </Col>
                    </Row>
                </div>
            </div>
            <Fragment>
                <Modal show={Basic} size="large">
                    <Modal.Header
                        closeButton
                        onClick={() => {
                            viewDemoClose("Basic")
                        }}
                    >
                        <h6>Basic Modal</h6>
                    </Modal.Header>
                    <Modal.Body>
                        <h6>Modal Body</h6>
                        There are many variations of passages of Lorem Ipsum
                        available, but the majority have suffered alteration.
                        <br />
                    </Modal.Body>
                    <Modal.Footer>
                        <Button
                            variant="primary"
                            onClick={() => {
                                viewDemoClose("Basic")
                            }}
                            className="text-center"
                        >
                            cantainue
                        </Button>
                        <Button
                            variant="danger"
                            onClick={() => {
                                viewDemoClose("Basic")
                            }}
                            className="text-center"
                        >
                            Close
                        </Button>
                    </Modal.Footer>
                </Modal>
            </Fragment>
        </React.Fragment >
    )
}
