import React from 'react'
import { Button, Card, Col, Row } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom';
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function CaseOverview() {

    const navigate = useNavigate();

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Project Info" BreadcrumbItemList={[{ name: 'Project Info' }]} />

            <Row className="row row-sm">
                <Col lg={{ span: 3 }}>
                    <Card className="custom-card">
                        <Card.Body className="user-card text-center">
                            <div className="icon-service bg-info-transparent rounded-circle text-success">
                                <i className="fe fe-book"></i>
                            </div>
                            <div className="mt-2">
                                <h5 className="mb-1">Overview</h5>
                            </div>
                            <Button
                                variant="success"
                                type="button"
                                className="btn mt-3 me-3 mb-0 btn-icon-text"
                                onClick={() => navigate('/case-info/overview/')}
                            >
                                <i className="fe fe-external-link me-2"></i> View Page
                            </Button>
                            <Button
                                variant="light"
                                type="button"
                                className="btn mt-3 btn-icon-text"
                            >
                                <i className="fa fa-wrench me-2"></i> Set as Default
                            </Button>
                        </Card.Body>
                    </Card>
                </Col>
                <Col lg={3}>
                    <Card className="custom-card">
                        <Card.Body className="user-card text-center">
                            <div className="icon-service bg-info-transparent rounded-circle text-info">
                                <i className="fe fe-trending-up"></i>
                            </div>
                            <div className="mt-2">
                                <h5 className="mb-1">Project Processing</h5>
                            </div>
                            <Button
                                variant="info"
                                type="button"
                                className="btn mt-3 me-3 btn-icon-text"
                                onClick={() => navigate('/case-info/process/')}
                            >
                                <i className="fe fe-external-link me-2"></i> View Page
                            </Button>
                            <Button
                                variant="light"
                                type="button"
                                className="btn mt-3 btn-icon-text"
                            >
                                <i className="fa fa-wrench me-2"></i> Set as Default
                            </Button>
                        </Card.Body>
                    </Card>
                </Col>
                <Col lg={{ span: 3 }}>
                    <Card className="custom-card">
                        <Card.Body className="user-card text-center">
                            <div className="icon-service bg-primary-transparent rounded-circle text-primary">
                                <i className="fas fa-newspaper"></i>
                            </div>
                            <div className="mt-2">
                                <h5 className="mb-1">Project Specific Data</h5>
                            </div>
                            <Button
                                variant="primary"
                                type="button"
                                className="btn mt-3 me-3 btn-icon-text"
                                onClick={() => navigate('/case-info/specific/')}
                            >
                                <i className="fe fe-external-link me-2"></i> View Page
                            </Button>
                            <Button
                                variant="light"
                                type="button"
                                className="btn mt-3 btn-icon-text"
                            >
                                <i className="fa fa-wrench me-2"></i> Set as Default
                            </Button>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </React.Fragment>
    )
}
