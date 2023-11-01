import React from "react";
import { Button, Card, Col, Row } from "react-bootstrap"
import { v4 as uuidv4 } from 'uuid';
import { useState } from "react";

export function OperationalReports({user_type}) {
    const attorney = [
        "Weekly Target File Date Report",
        "Attorney Review Project Report",
        "Open Projects Report",
        "Paralegal Workload Report",
        "PR Process Initiation Report",
        "Document Expiration Report",
        "Priority Date Report",
        "Data Audit Report"
    ]
    const paralegal = [
        "Weekly Target File Date Report",
        "Open Projects Report",
        "Paralegal Workload Report",
        "Data Audit Report"
    ]
    const hr = [
        "Open Projects Report",
        "New Hire Report",
        "PR Process Initiation Report",
        "Document Expiration Report",
        "Priority Date Report"
    ]
    let data_list = attorney
    if(user_type==='hr') {
        data_list = hr
    } else if(user_type==='paralegal') {
        data_list = paralegal
    }
    // eslint-disable-next-line no-unused-vars
    const [list, setList] = useState(data_list);

    return <Card className="custom-card static-card">
        <Card.Body className="">
            <h5 className="main-content-label">Operational Reports</h5>
            <Row className=" row-sm">
                {list.map(item => {
                    return <Col md={3} xl={3} className='mb-4' key={uuidv4()}>
                        <Button variant="primary" className="btn-custom btn-block tx-15 ht-70 bg-gradient">{item}</Button>
                    </Col>
                })}
            </Row>
        </Card.Body>
    </Card>
}

export function ComplianceReports({user_type}) {
    // console.log(user_type)
    const att_para_list = [
        "Employee Worksite Report",
        "LCA PAF Purge Report",
        "LCA PAF and PERM Audit File Report",
        "SLA Report",
        "240-Day Rule Report"
    ]
    const hr_list = [
        "Employee Worksite Report",
        "LCA PAF Purge Report",
        "LCA PAF and PERM Audit File Report",
        "SLA Report"
    ]

    let data_list = att_para_list
    if(user_type==='hr') {
        console.log("hereee")
        console.log(user_type)
        data_list = hr_list
    }
    else{
        console.log("asfsdgs")
    }

    // eslint-disable-next-line no-unused-vars
    const [list, setList] = useState(
        data_list
    );

    return <Card className="custom-card static-card">
        <Card.Body className="">
            <h5 className="main-content-label">Compliance Reports</h5>
            <Row className=" row-sm">
                {list.map(item => {
                    return <Col md={3} xl={3} className='mb-3' key={uuidv4()}>
                        <Button variant={"primary"} className="btn-custom btn-block tx-15 ht-70 bg-gradient">{item}</Button>
                    </Col>
                })}
            </Row>
        </Card.Body>
    </Card>
}

export function PerformanceMetricsReport(user_type) {
    
    // eslint-disable-next-line no-unused-vars
    const [list, setList] = useState(
        [
            "Project Preparation Metrics",
            "Productivity Metrics",
            "Net Profitability Metrics",
            "Cost of Production Metrics"

        ]
    );

    return <Card className="custom-card static-card">
        <Card.Body className="">
            <h5 className="main-content-label">Performance Metrics Report</h5>
            <Row className=" row-sm">
                {list.map(item => {
                    return <Col md={3} xl={3} className='mb-3' key={uuidv4()}>
                        <Button variant="primary" className="btn-custom btn-block tx-15 ht-70 bg-gradient">{item}</Button>
                    </Col>
                })}
            </Row>
        </Card.Body>
    </Card>
}
