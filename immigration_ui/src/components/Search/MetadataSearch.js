import React, { Fragment } from 'react';
import { Col, Row, Form, InputGroup, Button, } from 'react-bootstrap';
import { Datepicker } from './DatePicker';


const MetaDataSearch = () => {
    return (<Fragment>
        
        <Row className="row-sm">
            <Form className='search-form'>
                <Row>
                    <Col lg={4}>
                        <InputGroup className="mb-3">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-1">Metadata Field-1</InputGroup.Text>
                            <Form.Control placeholder='Robert' />
                        </InputGroup>
                    </Col>
                    <Col lg={4}>
                        <InputGroup className="mb-3 d-flex flex-row">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-2">Metadata Field-2</InputGroup.Text>
                            <div style={{ width: '60%' }}><Datepicker></Datepicker></div>
                        </InputGroup>
                    </Col>
                    <Col lg={4}>
                        <InputGroup className="mb-3">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-3" >Metadata Field-3</InputGroup.Text>
                            <Form.Control placeholder='Project ID' />
                        </InputGroup>
                    </Col>
                </Row>
                <Row>
                    <Col lg={4}>
                        <InputGroup className="mb-3">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-4">Metadata Field-4</InputGroup.Text>
                            <Form.Control placeholder='' />
                        </InputGroup>
                    </Col>
                    <Col lg={4}>
                        <InputGroup className="mb-3 d-flex flex-row">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-5">Metadata Field-5</InputGroup.Text>
                            <div style={{ width: '60%' }}><Datepicker></Datepicker></div>
                        </InputGroup>
                    </Col>
                    <Col lg={4}>
                        <InputGroup className="mb-3">
                            <InputGroup.Text className="input-group-text" aria-label="Metadata Field-6" >Metadata Field-6</InputGroup.Text>
                            <Form.Control placeholder='' />
                        </InputGroup>
                    </Col>
                </Row>

            </Form>
            {/* </Col> */}
        </Row>
        <div className='d-flex align-center'>
            <Button
                variant="primary " className='btn btn-primary btn-md btn-block'
            // onClick={() => setSearchBeneficiaryModal(false)}
            >
                <i className="fa fa-search"></i> Search
            </Button>
        </div>
    </Fragment>
    )
};

MetaDataSearch.propTypes = {};

MetaDataSearch.defaultProps = {};

export default MetaDataSearch;
