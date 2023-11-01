import React from 'react'
import { Badge, Button, Card, Col, Row } from 'react-bootstrap'
import { Line } from 'react-chartjs-2';
import * as overviewGraph from "./OverviewGraph/OverviewGraph";
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function CaseOverview() {
    
    const checkTypeAttorney = () => localStorage.getItem('user_type') === "attorney" ? true : false;

    const attorney = {
        openCases: [{ name: "Firm Projects", count: 55 }, { name: "My Projects", count: 6 }],
        averagePreparationTime: [{ name: "Standard Firm SLA", count: 55 }, { name: "Firm Projects", count: 15 }, { name: "My Projects", count: 10 }]
    }

    const paralegal = {
        openCases: [{ name: "Firm Projects", count: 55 }, { name: "My Projects", count: 6 }],
        averagePreparationTime: [{ name: "Standard Firm SLA", count: 55 }, { name: "My Projects", count: 10 }]
    }

    const hr = {
        openCases: [{ name: "Open Projects", count: 55 }],
        averagePreparationTime: [{ name: "Standard Firm SLA", count: 55 }, { name: "My Projects", count: 10 }]
    }

    let data = []

    const DataCard = (props) => {
        const user_type = 'attorney'
        switch (user_type) {
            case 'attorney':
                data = attorney
                break
            case 'paralegal':
                data = paralegal
                break
            case 'hr':
                data = hr
                break
            default:
                break
        }
        switch (props.type) {
            case 'openCases':
                data = data.openCases
                break
            case 'averagePreparationTime':
                data = data.averagePreparationTime
                break
            default:
                break
        }

        return <div className="d-flex flex-column mt-3">
            <table className="case-overview-table">
                <tbody>
                    {data.map((item, index) => (
                        <tr key={index}>
                            <td>
                                <div className="td">
                                    <h5 className="main-content-label">{item.name}</h5>
                                    <h3 className="badge-mark"><Badge bg="dark">{item.count}</Badge></h3>
                                </div>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Project Overview" BreadcrumbItemList={[{ name: 'Project Info', link: '/case-info/' }, { name: "Project Overview" }]} />

            <div className='case-overview-priority-container'>
                <Row className="row row-sm row-tiles">
                    <Col lg={3}>
                        <Card className="custom-card">
                            <Card.Body className="user-card text-center">
                                <div className="icon-service bg-info-transparent rounded-circle text-info">
                                    <i className="fe fe-trending-up"></i>
                                </div>
                                <div className="mt-2">
                                    <h5 className="mb-1">Total Open Projects</h5>
                                    <p className="mb-0 text-muted">
                                        Includes total open firm Projects & assignee
                                    </p>
                                </div>
                                <DataCard type="openCases" />
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col lg={3}>
                        <Card className="custom-card">
                            <Card.Body className="user-card text-center">
                                <div className="icon-service bg-warning-transparent rounded-circle text-warning">
                                    <i className="fe fe-git-pull-request"></i>
                                </div>
                                <div className="mt-2">
                                    <h5 className="mb-1">Average Preparation Time</h5>
                                    <p className="mb-0 text-muted">
                                        From Info/Docs Requested to Project Filing
                                    </p>
                                </div>
                                <DataCard type="averagePreparationTime" />
                            </Card.Body>
                        </Card>
                    </Col>
                    <Col lg={3}>
                        <Card className="custom-card">
                            <Card.Body className="user-card text-center">
                                <div className="icon-service bg-info-transparent rounded-circle text-info">
                                    <i className="fe fe-arrow-down"></i>
                                </div>
                                <div className="mt-2">
                                    <h5 className="mb-1">Average Preparation Time</h5>
                                    <p className="mb-0 text-muted">
                                        From Info/Docs Received to Project Filing
                                    </p>
                                </div>
                                <DataCard type="averagePreparationTime" />
                            </Card.Body>
                        </Card>
                    </Col>
                    {checkTypeAttorney() &&
                        <Col lg={3}>
                            <Card className="custom-card">
                                <Card.Body className="user-card text-center">
                                    <div className="icon-service bg-primary-transparent rounded-circle text-primary">
                                        <i className="fe fe-trending-up"></i>
                                    </div>
                                    <div className="mt-2">
                                        <h5 className="mb-1">Projects Missed SLA</h5>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    }
                </Row>
                <Row className='row-priority'>
                    {checkTypeAttorney() &&
                        <Col lg={{ span: 4, offset: 0 }}>
                            <Card className="custom-card">
                                <Card.Header className=" border-bottom-0 pb-0 d-flex ps-3 ms-1">
                                    <div>
                                        <label className="main-content-label mb-2">
                                            preparation - Projects to Prioritize - Mar-Apr
                                        </label>
                                        <span className="d-block tx-12 mb-2 text-muted">
                                            Projects where development work is on completion
                                        </span>
                                    </div>
                                </Card.Header>
                                <Card.Body className="pt-2 mt-0">
                                    <div className='case-overview-priority-container'>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Current Week</h6>
                                            <h6 className='count'>Count - 10</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 13-Mar</h6>
                                            <h6 className='count'>Count - 55</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 20-Mar</h6>
                                            <h6 className='count'>Count - 999</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 27-Mar</h6>
                                            <h6 className='count'>Count - 500</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    }
                    {checkTypeAttorney() &&
                        <Col lg={4}>
                            <Card className="custom-card">
                                <Card.Header className=" border-bottom-0 pb-0 d-flex ps-3 ms-1">
                                    <div>
                                        <label className="main-content-label mb-2">
                                            Filings - Projects to Prioritize - Mar-Apr
                                        </label>
                                        <span className="d-block tx-12 mb-2 text-muted">
                                            Projects where development work is on completion
                                        </span>
                                    </div>
                                </Card.Header>
                                <Card.Body className="pt-2 mt-0">
                                    <div className='case-overview-priority-container'>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Current Week</h6>
                                            <h6 className='count'>Count - 10</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 13-Mar</h6>
                                            <h6 className='count'>Count - 55</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 20-Mar</h6>
                                            <h6 className='count'>Count - 999</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                        <div className='priority-box'>
                                            <h6 className='week-of'>Week of 27-Mar</h6>
                                            <h6 className='count'>Count - 500</h6>
                                            <Button
                                                variant="light"
                                                type="button"
                                                className="btn btn-icon-text"
                                            >
                                                <i className="fe fe-external-link me-2"></i> View
                                            </Button>
                                        </div>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    }
                    <Col lg={4}>
                        <Card className="custom-card">
                            <Card.Header className=" border-bottom-0 pb-0 d-flex ps-3 ms-1">
                                <div>
                                    <label className="main-content-label mb-2">
                                        Open Projects by Secondary Project Status (Graph)
                                    </label>
                                </div>
                            </Card.Header>
                            <Card.Body>
                                <div className="chart-wrapperchart-dropshadow2">
                                    <Line options={overviewGraph.currentYearOptions} data={overviewGraph.currentYearData} className="barchart chart-dropshadow2 chartjs-render-monitor" height={300} />
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        </React.Fragment>
    )
}
