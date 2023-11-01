import React, { Fragment } from 'react'
import { Col, Row, Form, InputGroup, ListGroup, Modal, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { Datepicker } from './DatePicker'
import { v4 as uuidv4 } from 'uuid'
import { Link, useLocation } from 'react-router-dom'
import { setBeneficiarySearchModal } from 'store/slices/commonSlice'
import { actions } from 'store/slices/beneficiarySlice'

const BasicSearch = () => {
    const commonStore = useSelector((state) => {
        return state['common']
    })

    const dispatch = useDispatch()

    const initialState = useSelector((state) => state.beneficiary.profileData.beneficiaryList)
    const { search } = useLocation()

    const selectBeneficiary = (beneficiary) => {
        const _data = {
            id: beneficiary.BeneficiaryID,
            name: beneficiary.BeneficiaryName
        }

        dispatch(actions.setBeneficiary(_data))
        dispatch(setBeneficiarySearchModal(false))
    }

    console.log('search:', search)

    return (
        <Fragment>
            <Modal show={commonStore.beneficiarySearchModal.isOpen} size="md" backdrop="false">
                <Modal.Header closeButton onClick={() => dispatch(setBeneficiarySearchModal(false))}>
                    <Modal.Title>Search</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Row className="row-sm">
                        <Col lg={12}>
                            <Form className="search-form">
                                <InputGroup className="mb-3">
                                    <InputGroup.Text className="input-group-text" aria-label="Beneficiary-Name">
                                        Beneficiary Name
                                    </InputGroup.Text>
                                    <Form.Control placeholder="Beneficiary Name" />
                                </InputGroup>
                                <InputGroup className="mb-3 d-flex flex-row">
                                    <InputGroup.Text className="input-group-text" aria-label="DOB">
                                        DOB
                                    </InputGroup.Text>
                                    <div style={{ width: '60%' }}>
                                        <Datepicker></Datepicker>
                                    </div>
                                </InputGroup>
                                <InputGroup className="mb-3">
                                    <InputGroup.Text className="input-group-text" aria-label="Case-Id">
                                        Project ID
                                    </InputGroup.Text>
                                    <Form.Control placeholder="Project ID" />
                                </InputGroup>
                                <InputGroup className="mb-3">
                                    <InputGroup.Text className="input-group-text" aria-label="Petitioner-Name">
                                        Petitioner Name
                                    </InputGroup.Text>
                                    <Form.Control placeholder="Petitioner Name" />
                                </InputGroup>
                            </Form>
                        </Col>
                    </Row>
                    <Row>
                        <Col lg={12}>
                            <ListGroup className="task-list-group beneficiary-search-result">
                                {initialState?.beneficiary?.map((item) => {
                                    return (
                                        <ListGroup.Item
                                            action
                                            className="flex-column align-items-start p-2"
                                            key={uuidv4()}
                                        >
                                            <div className="d-flex w-100 justify-content-between">
                                                <h6 className="font-weight-semibold ">{item.BeneficiaryName}</h6>
                                                <div className="d-flex justify-content-between">
                                                    <Link to={`./${search}`} onClick={() => selectBeneficiary(item)}>
                                                        Select
                                                    </Link>
                                                </div>
                                            </div>
                                        </ListGroup.Item>
                                    )
                                })}
                            </ListGroup>
                        </Col>
                    </Row>
                </Modal.Body>
                <Modal.Footer>
                    <Button
                        variant="primary"
                        // onClick={() => setSearchBeneficiaryModal(false)}
                    >
                        <i className="fa fa-search"></i> Search
                    </Button>
                    <Button variant="secondary" onClick={() => dispatch(setBeneficiarySearchModal(false))}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>
        </Fragment>
    )
}

BasicSearch.propTypes = {}

BasicSearch.defaultProps = {}

export default BasicSearch
