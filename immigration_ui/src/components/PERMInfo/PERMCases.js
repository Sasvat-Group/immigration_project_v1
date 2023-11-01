import React from 'react'
import { Card, Col, Row } from 'react-bootstrap'
import './PermCase.style.scss'
import Stepper from 'components/Common/Stepper'
import PageHeader from 'layouts/PageHeader/PageHeader'

export default function PERMCases() {

    // eslint-disable-next-line no-unused-vars
    const DurationCard = ({ color }) => {
        return (<Card className="duration-card">
            <Card.Header className='p-2' style={{ backgroundColor: color, color: '#fff' }}>
                Duration
            </Card.Header>
            <Card.Body>
                <div className="label-container">
                    <h5><small>Project Initiation Date:</small> 11/1/2017</h5>
                </div>
                <div className="label-container">
                    <h5><small>End Date (ETA):</small> 11/1/2017</h5>
                </div>
                <div className="label-container">
                    <h5><small>Phase Duration: </small> 14 Days</h5>
                </div>
                <div className="label-container">
                    <h5><small>Status: </small>Completed</h5>
                </div>
            </Card.Body>
        </Card>)
    }

    const stepswizard = [
        {
            name: "Initiation", color: '#6259ca', indexValue: 'O', list: [
                'Project initiated',
                `Waiting for JD and MR from Manager/Company`
            ]
        },
        {
            name: "Finalize AD Text, JD, MR And PWR", color: '#5952b6', indexValue: 'I',
            list: [
                'Prepare PERM Ad Text, JD and MR',
                'Finalize PERM Ad Text, JD and MR with Company',
                'Prepare Work Experience Chart for Employee to complete',
                'Prepare draft EVL(s) to be obtained by Employee',
                `Receive signed EVL(s) or confirmation that Employee\n
                will be able to obtain EVL(s)`,
                'Prepare PWR for Company\'s review and approval',
                'Submit PWR with DOL'
            ]
        },
        { name: "PWR Pending With DOL", color: '#4c4799', indexValue: 'II', list: ['Awaiting PWD from DOL'] },
        {
            name: "In Recruitment", color: '#403d7d', indexValue: 'III', list: [
                'Receive PWD from DOL', 'Begin PERM Recruitment'
            ]
        },
        { name: "Quite Period", color: '#31325d', indexValue: 'IV', list: ['DOL Requirement'] },
        {
            name: "Prepare Project For Filing", color: '#272945', indexValue: 'V', list: [
                'Receive Recruitment Results Tracker from Company',
                'Receive Recruitment Results Report from Company',
                `Receive Approval from
            Company to Proceed with the Project`,
                `Draft ETA Form 9089 for
            Employee and Company's Review`,
                'Finalize and File ETA Form 9089 with DOL'
            ]
        },
        {
            name: "ETA Firm 9089 Filed And Pending", color: '#1d212f', indexValue: 'VI', list: [
                'PERM Application Pending with DOL'
            ]
        },
    ]

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="PERM Projects" BreadcrumbItemList={[{ name: 'PERM Info' }, { name: 'PERM Projects' }]} />

            <Row className="row-sm perm-case-container">
                <Col xl={12}>
                    <Card>
                        <Card.Body>
                            <h6 className='mb-4'>
                                Employee Name: Hector Barbosa | PERM Initiation Date: 11/01/2017
                            </h6>
                            <Stepper data={stepswizard} allowList={true} />
                            <div className="flex-1 d-flex flex-row align-items-center justify-content-between mt-3 px-0">
                                {stepswizard.map((step, index) => <DurationCard key={index} color={step.color} />)}
                            </div>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </React.Fragment>
    )
}