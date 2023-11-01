import React from "react";
import { Button, Card, Col, Form, InputGroup, Nav } from "react-bootstrap";
import { SidePetitionerList } from "./SidePetitionerList";

export default function PetitionerList() {
    return (
        <Col md={3} sm={4}>
            <Card className="custom-card card-scrollable">
                <div className="main-content-app pt-0">
                    <div className="main-content-left main-content-left-chat">
                        <Card.Header className="px-0">
                            <InputGroup className="px-4 pt-0 pb-4 border-bottom">
                                <Form.Control type="text" className="form-control" placeholder="Petitioner ..." />
                                <span>
                                    <Button variant="primary" className="btn ripple btn-primary" type="button">
                                        Search
                                    </Button>
                                </span>
                            </InputGroup>
                        </Card.Header>
                        <Card.Body className="p-0">
                            <Nav variant="pills" className="item1-links flex-column nav panel-tabs">
                                <SidePetitionerList />
                            </Nav>
                        </Card.Body>
                    </div>
                </div>
            </Card>
        </Col>
    );
}
