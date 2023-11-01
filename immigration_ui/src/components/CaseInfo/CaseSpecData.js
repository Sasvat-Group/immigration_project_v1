import React, { Fragment, useEffect } from 'react'
import { Card } from 'react-bootstrap'
import CollapsibleTable from 'components/CTable/CTable1'
import { useLocation } from 'react-router-dom'
import PageHeader from 'layouts/PageHeader/PageHeader'

const CostSpecData = () => {
    const location = useLocation()

    useEffect(() => {
        // console.log(location.state.caseType)
    }, [])

    return (
        <Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader
                Header="Project Specific Data"
                BreadcrumbItemList={[{ name: 'Project Info', link: '/case-info/' }, { name: 'Project Specific Data' }]}
            />

            {/* <!-- Row --> */}
            <Card className="custom-card">
                <Card.Body>
                    <h6 className="main-content-label mb-1">Project Data</h6>
                    <p className="text-muted  card-sub-title">
                        Based on your search parameter you will get the Project Data.
                    </p>
                    <CollapsibleTable state={location.state}></CollapsibleTable>
                </Card.Body>
            </Card>
            {/* <Row className=" row-sm">
      <Col md={12}>
        <Card className="custom-card overflow-hidden">
          <Card.Body className="card-body">
            <div>
              <h6 className="main-content-label mb-1">Line Chart</h6>
              <p className="text-muted  card-sub-title">
                Below is the basic line chart example.
              </p>
            </div>
            <div className="chartjs-wrapper-demo">
              <Line
                options={chart.Linechart}
                data={chart.linechartdata}
                className="barchart"
                height="250"
              />
            </div>
          </Card.Body>
        </Card>
      </Col>
    </Row> */}
        </Fragment>
    )
}

CostSpecData.propTypes = {}

CostSpecData.defaultProps = {}

export default CostSpecData
