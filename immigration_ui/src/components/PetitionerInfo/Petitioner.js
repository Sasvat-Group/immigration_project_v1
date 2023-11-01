/* eslint-disable react-hooks/exhaustive-deps */
import PageHeader from "layouts/PageHeader/PageHeader"
import React from "react"
import { Card, Col, Row, Tab } from "react-bootstrap"
import { v4 as uuid } from "uuid"
import PetitionerList from "./PetitionerList"
import { ProfileSection } from "./ProfileSection"

const TabContainer = React.lazy(() => import("./TabContainer"))

export default function Petitioner() {

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Petitioner Details" BreadcrumbItemList={[{ name: "Petitioner Info", link: "/petitioner-info/" }, { name: "Petitioner Details" }]} />

            <div className="petitioner-container">
                <Row className="row-sm">
                    <Col lg={12}>
                        <div className="panel panel-primary ">
                            <div className="tab-menu-heading">
                                <div className="tabs-menu">
                                    <Tab.Container id="left-tabs-example" defaultActiveKey="0">
                                        <Row>
                                            <PetitionerList />
                                            <Col md={9} sm={8} className="border-start">
                                                <Tab.Content className="panel-body tabs-menu-body">
                                                    <Tab.Pane key={uuid()} eventKey={0} className="pt-0">
                                                        <Tab.Container id="center-tabs-example" defaultActiveKey="Overview" className="bg-gray-100">
                                                            <ProfileSection />
                                                            <Row className="row-sm">
                                                                <div className="card custom-card main-content-body-profile">
                                                                    <Card className="custom-card main-content-body-profile mb-0">
                                                                        <div className="tab-content">
                                                                            <TabContainer />
                                                                        </div>
                                                                    </Card>
                                                                </div>
                                                            </Row>
                                                        </Tab.Container>
                                                    </Tab.Pane>
                                                </Tab.Content>
                                            </Col>
                                        </Row>
                                    </Tab.Container>
                                </div>
                            </div>
                        </div>
                    </Col>
                </Row>
            </div>
        </React.Fragment>
    )
}
