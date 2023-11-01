import React from 'react'
import { Accordion, Card, Col, Row, Table } from 'react-bootstrap'
import { v4 as uuid4 } from 'uuid';
import { useState } from 'react';
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function PERMOverall() {

    // eslint-disable-next-line no-unused-vars
    const [employees, setEmployees] = useState([
        {
            employeeName: 'Employee 1',
            employeeID: 46465126,
            outsideCounsel: '',
            foreignNationalID: 5415555,
            actionToBeTaken: '',
            actionToBeTakenBy: '',
            dueDateToCompleteAction: '',
        },
        {
            employeeName: 'Employee 2',
            employeeID: 46465126,
            outsideCounsel: '',
            foreignNationalID: 5415555,
            actionToBeTaken: '',
            actionToBeTakenBy: '',
            dueDateToCompleteAction: '',
        },
        {
            employeeName: 'Employee 3',
            employeeID: 46465126,
            outsideCounsel: '',
            foreignNationalID: 5415555,
            actionToBeTaken: '',
            actionToBeTakenBy: '',
            dueDateToCompleteAction: '',
        },
        {
            employeeName: 'Employee 4',
            employeeID: 46465126,
            outsideCounsel: '',
            foreignNationalID: 5415555,
            actionToBeTaken: '',
            actionToBeTakenBy: '',
            dueDateToCompleteAction: '',
        },
        {
            employeeName: 'Employee 5',
            employeeID: 46465126,
            outsideCounsel: '',
            foreignNationalID: 5415555,
            actionToBeTaken: '',
            actionToBeTakenBy: '',
            dueDateToCompleteAction: '',
        }
    ]);

    const SubRow = () => {

        return (<React.Fragment>
            <tr>
                <td>Employee (Last Name, First Name)</td>
                <td>Employee 1</td>
                <td>Employee 2</td>
                <td>Employee 3</td>
                <td>Employee 4</td>
                <td>Employee 5</td>
                <td>Employee 6</td>
            </tr>
            <tr>
                <td>Employee Identification</td>
                <td>Employee 1</td>
                <td>Employee 2</td>
                <td>Employee 3</td>
                <td>Employee 4</td>
                <td>Employee 5</td>
                <td>Employee 6</td>
            </tr>
            <tr>
                <td>Outside Counsel Firm Name</td>
                <td>Employee 1</td>
                <td>Employee 2</td>
                <td>Employee 3</td>
                <td>Employee 4</td>
                <td>Employee 5</td>
                <td>Employee 6</td>
            </tr>
            <tr>
                <td>Foreign National Identification</td>
                <td>Employee 1</td>
                <td>Employee 2</td>
                <td>Employee 3</td>
                <td>Employee 4</td>
                <td>Employee 5</td>
                <td>Employee 6</td>
            </tr>
        </React.Fragment>);
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="PERM Overall" BreadcrumbItemList={[{ name: 'PERM Info' }, { name: 'PERM Overall' }]} />

            <div className="perm-overall-container">
                <Row>
                    <Col xl={12}>
                        <Card className="custom-card">
                            <Card.Body>
                                <h5 className="main-content-label">Projects Requiring Immediate Attention</h5>
                                <Table className="text-nowrap table-bordered table-striped mt-3">
                                    <thead>
                                        <tr>
                                            <th>Employee Name</th>
                                            <th>Employee ID</th>
                                            <th>Outside Counsel</th>
                                            <th>Foreign National ID</th>
                                            <th>Action to be Taken</th>
                                            <th>Action to be Taken By</th>
                                            <th>Due Date to Complete Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {employees.map(employee => {
                                            return <tr key={uuid4()}>
                                                <td>{employee.employeeName}</td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                        })}
                                    </tbody>
                                </Table>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
                <Row>
                    <Col xl={12}>
                        <Card className="custom-card">
                            <Card.Body>
                                <h5 className="main-content-label mb-3">Projects 'In Recruitment'</h5>
                                <Accordion defaultActiveKey="0" alwaysOpen onChange={() => {
                                    console.log('chaned')
                                }}>
                                    <Accordion.Item eventKey="0">
                                        <Accordion.Header onClick={() => { console.log('x') }}>
                                            General Info
                                        </Accordion.Header>
                                        <Accordion.Body>
                                            <Table className="text-nowrap table-bordered">
                                                <tbody>
                                                    <SubRow />
                                                </tbody>
                                            </Table>
                                        </Accordion.Body>
                                    </Accordion.Item>
                                    <Accordion.Item eventKey="1">
                                        <Accordion.Header>Key Dates</Accordion.Header>
                                        <Accordion.Body>
                                            <Table className="text-nowrap table-bordered">
                                                <tbody>
                                                    <SubRow />
                                                </tbody>
                                            </Table>
                                        </Accordion.Body>
                                    </Accordion.Item>
                                    <Accordion.Item eventKey="2">
                                        <Accordion.Header>Recruiment Methods Completed by Outside Counsel</Accordion.Header>
                                        <Accordion.Body>
                                            <Table className="cases-recruitment-table text-nowrap text-md-nowrap table-bordered">
                                                <tbody>
                                                    <SubRow />
                                                </tbody>
                                            </Table>
                                        </Accordion.Body>
                                    </Accordion.Item>
                                </Accordion>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </div>
        </React.Fragment>
    )
}