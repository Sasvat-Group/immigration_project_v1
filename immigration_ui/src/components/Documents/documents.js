import React, { Fragment } from 'react';
import PageHeader from 'layouts/PageHeader/PageHeader';
import { Button, Col, Row, Card, Form, Table } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const docList = [{
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-01",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-02",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-03",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-04",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-05",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-06",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-07",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}, {
    "doc_name": "Document - test-document-of-the search-result-test-document-of-the search-result-08",
    "doc_link": "#",
    "updated_date": "23-Apr-2023 05:00 PM"
}]

const Documents = () => {
    const user_type = localStorage.getItem('user_type')

    function type_rendering(user_type){
        if(user_type === "attorney" || user_type === "paralegal") {
            return (
                <Fragment>
                <Col lg={12}>
                <Card className="custom-card">
                    <Card.Body>
                        <h5 className="main-content-label">Firm Knowledge Management <i className="fe fe-link text-primary"></i></h5>
                        <div className="btn-list mt-3">
                            <Button variant="outline-primary" type="button" className="btn-block">SharePoint Site</Button>
                            <Button variant="outline-secondary" type="button" className="btn-block">FAQs</Button>
                            <Button variant="outline-success" type="button" className="btn-block">Process Workflows</Button>
                            <Button variant="outline-info" type="button" className="btn-block">Key Templates</Button>
                            <Button variant="outline-danger" type="button" className="btn-block">Training Videos</Button>
                        </div>
                    </Card.Body>
                </Card>
            </Col>
            <Col lg={12}>
                <Card className="custom-card">
                    <Card.Body>
                        <div>
                            <h5 className="main-content-label">Petitioner/Beneficiary Folders <i className="fe fe-link text-primary"></i></h5>
                            <div className="btn-list mt-3">
                                <Button variant="outline-primary" type="button" className="btn-block">Company</Button>
                                <Button variant="outline-secondary" type="button" className="btn-block">Supporting Documents</Button>
                                <Button variant="outline-success" type="button" className="btn-block">Notices</Button>
                                <Button variant="outline-info" type="button" className="btn-block">Immigration Filings</Button>
                                <Button variant="outline-danger" type="button" className="btn-block">Beneficiary Workspace</Button>
                            </div>
                        </div>
                    </Card.Body>
                </Card>
            </Col>
            </Fragment>
            )
        }
        else if(user_type==="hr"){
            return (
                <Fragment>
                <Col lg={12}>
                <Card className="custom-card">
                    <Card.Body>
                        <h5 className="main-content-label">Client Knowledge Management <i className="fe fe-link text-primary"></i></h5>
                        <div className="btn-list mt-3">
                            <Button variant="outline-success" type="button" className="btn-block">Process Workflows</Button>
                            <Button variant="outline-secondary" type="button" className="btn-block">FAQs</Button>
                            <Button variant="outline-danger" type="button" className="btn-block">Training Videos</Button>
                        </div>
                    </Card.Body>
                </Card>
            </Col>
            </Fragment>
            )
        }
    }

    // const treeviewData = [
    //     {
    //         id: "Xrp",
    //         text: "XRP",
    //         children: [
    //             {
    //                 id: "XrpCompanyMaintenance",
    //                 text: "Company Maintenance",
    //                 isLeaf: true,
    //             },
    //             {
    //                 id: "XrpEmployees",
    //                 text: "Employees",
    //                 children: [
    //                     {
    //                         id: "XrpReports",
    //                         text: "Reports",
    //                         isLeaf: true,
    //                     },
    //                 ],
    //             },
    //             {
    //                 id: "XrpHumanResources",
    //                 text: "Human Resources",
    //                 isLeaf: true,
    //             },
    //         ],
    //     },
    // ];

    return (
        <Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Documents" BreadcrumbItemList={[{ name: 'Documents' }]} />

            {/* <!-- Row --> */}
            <Row>
                <Col lg={3}>
                    <Row>
                        {type_rendering(user_type)}
                        {/* <Col lg={12}>
                            <Card className="custom-card">
                                <Card.Body>
                                    <h5 className="main-content-label">Firm Knowledge Management <i className="fe fe-link text-primary"></i></h5>
                                    <div className="btn-list mt-3">
                                        <Button variant="outline-primary" type="button" className="btn-block">SharePoint Site</Button>
                                        <Button variant="outline-secondary" type="button" className="btn-block">FAQs</Button>
                                        <Button variant="outline-success" type="button" className="btn-block">Process Workflows</Button>
                                        <Button variant="outline-info" type="button" className="btn-block">Key Templates</Button>
                                        <Button variant="outline-danger" type="button" className="btn-block">Training Videos</Button>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col lg={12}>
                            <Card className="custom-card">
                                <Card.Body>
                                    <div>
                                        <h5 className="main-content-label">Petitioner/Beneficiary Folders <i className="fe fe-link text-primary"></i></h5>
                                        <div className="btn-list mt-3">
                                            <Button variant="outline-primary" type="button" className="btn-block">Company</Button>
                                            <Button variant="outline-secondary" type="button" className="btn-block">Supporting Documents</Button>
                                            <Button variant="outline-success" type="button" className="btn-block">Notices</Button>
                                            <Button variant="outline-info" type="button" className="btn-block">Immigration Filings</Button>
                                            <Button variant="outline-danger" type="button" className="btn-block">Beneficiary Workspace</Button>
                                        </div>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col> */}
                    </Row>
                </Col>
                <Col lg={9}>
                    <Card className="custom-card">
                        <Card.Body>
                            <h5 className="main-content-label">Search Document <i className="fe fe-search text-primary"></i></h5>
                            <Row className="row-sm mt-3">
                                <Col md={10}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Search to retrieve document" />
                                    </Form.Group>
                                </Col>
                                <Col md={2}>
                                    <Form.Group className="form-group">
                                        <Button
                                            variant="primary"
                                            type="button"
                                            className="btn btn-block btn-icon-text"
                                        >
                                            <i className="fe fe-search me-2"></i> Search
                                        </Button>
                                    </Form.Group>
                                </Col>
                            </Row>
                            <Row className="row-sm">
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta One" />
                                    </Form.Group>
                                </Col>
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta Two" />
                                    </Form.Group>
                                </Col>
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta Three" />
                                    </Form.Group>
                                </Col>
                            </Row>
                            <Row className="row-sm">
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta One" />
                                    </Form.Group>
                                </Col>
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta Two" />
                                    </Form.Group>
                                </Col>
                                <Col md={4}>
                                    <Form.Group className="form-group">
                                        <Form.Control
                                            type="text" name="example-text-input" placeholder="Meta Three" />
                                    </Form.Group>
                                </Col>
                            </Row>
                            <Row className='align-items-center p-3'>
                                <Table className="table text-nowrap text-md-nowrap mg-b-0 border">
                                    <thead>
                                        <tr className='text-start'>
                                            <th>Document Name</th>
                                            <th>Updated Time</th>
                                            <th>Link</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {docList.map((list, index) => (
                                            <tr key={index} data-index={index}>
                                                <td className='text-start'>{list.doc_name}</td>
                                                <td className='text-start'>{list.updated_date}</td>
                                                <td className='text-start'><Link to={'./'}>View</Link></td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </Table>
                            </Row>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Fragment>);

};

Documents.propTypes = {};

Documents.defaultProps = {};

export default Documents;
