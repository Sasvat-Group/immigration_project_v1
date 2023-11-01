import React from 'react'
import { Row } from 'react-bootstrap'
import PageHeader from 'layouts/PageHeader/PageHeader'

export default function Integration() {

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Integration" BreadcrumbItemList={[{ name: 'Integration' }]} />

            <Row className="row-sm">
            </Row>
        </React.Fragment>
    )
}
