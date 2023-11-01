import React from 'react'
import { Button, Card, Col, Row } from 'react-bootstrap'
import './immigration-tools.style.scss';
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function ImmigrationToolkit() {

    const data = [{
        title: "I-94 Retrieval Tools",
        list: [{
            name: "Bulk I-94 Data Retrieval",
            link: ""
        }, {
            name: "Bulk I-94 Document Retrieval",
            link: ""
        }]
    }, {
        title: "USCIS Retrieval Tools",
        list: [{
            name: "Bulk USCIS Project Status Retrieval",
            link: ""
        }]
    }, {
        title: "LCA Tools",
        list: [{
            name: "Electronic LCA (ETA 9035) Posting",
            link: ""
        }, {
            name: "LCA (ETA 9035) Drafting",
            link: ""
        }, {
            name: "Certified LCA (ETA 9035) Download",
            link: ""
        }, {
            name: "LCA (ETA 9035) Data Extraction",
            link: ""
        }]
    }, {
        title: "Prevailing Wage Related Tools",
        list: [{
            name: "Prevailing Wage Info Determination (from FLCA Data Center)",
            link: ""
        }, {
            name: "PERM PWR (ETA 9141) Drafting",
            link: ""
        }, {
            name: "PERM PWD (ETA 9035) Data Extraction",
            link: ""
        }]
    }, {
        title: "Document Management Tool",
        list: [{
            name: "Incoming Document Management",
            link: ""
        }, {
            name: "Outgoing Document (Filings) Management",
            link: ""
        }]
    }]

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Immigration Toolkit" BreadcrumbItemList={[{ name: 'Immigration Toolkit' }]} />

            <div className='immigration-tools-container'>
                <Row>
                    {data.map((item, index) => (
                        <Col xl={3}>
                            <Card className="custom-card">
                                <Card.Body>
                                    <h5 className="main-content-label">{item.title} <i className="fe fe-link"></i></h5>
                                    <div className="btn-list">
                                        {item.list.map((link) => (
                                            <Button variant={index % 2 === 0 ? "primary" : "secondary"} type="button">{link.name}</Button>
                                        ))}
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            </div>
        </React.Fragment>
    )
}
