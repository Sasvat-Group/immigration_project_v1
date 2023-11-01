import React from 'react'
import { Card, Col, Row } from 'react-bootstrap'
import PageHeader from 'layouts/PageHeader/PageHeader'

export default function PERMInfo() {

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="PERM Information" BreadcrumbItemList={[{ name: 'PERM Info' }]} />

            <Row className="row-sm">
                <Col xl={12}>
                    <Card>
                        <Card.Body>
                            <h1>Hello</h1>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </React.Fragment>
    )
}
