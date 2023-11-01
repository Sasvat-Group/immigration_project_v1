import React from 'react'
import { Card, Col, ListGroup, Row } from 'react-bootstrap'
import './compliance-info.style.scss';
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function ComplianceInfo() {

    const data = [{
        title: "Employee Worksite Compliance Audit",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "240-Day Report",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "LCA List",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "LCA PAF Status",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "LCA PAF Purge Report",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "PERM Audit File Status",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "PERM Audit File Purge Report",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }, {
        title: "PERM Lay-off Analysis",
        list: [{ title: '' }, { title: '' }, { title: '' }, { title: '' }, { title: '' }]
    }]

    return (
        <React.Fragment>

            {/* <!-- Page Header --> */}
            <PageHeader Header="Compliance Info" BreadcrumbItemList={[{ name: 'Compliance Info' }]} />

            <div className='compliance-info-container'>
                <Row>
                    {data.map((item, index) => (
                        <Col xl={3} key={index}>
                            <Card className="custom-card">
                                <Card.Header className={`p-3 tx-medium my-auto tx-white ${index % 2 === 0 ? "bg-primary" : "bg-secondary"}`}>
                                    {item.title}
                                </Card.Header>
                                <Card.Body>
                                    <ListGroup className='task-list-group'>
                                        {item.list.map(i => <ListGroup.Item></ListGroup.Item>)}
                                    </ListGroup>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            </div>
        </React.Fragment >
    )
}
