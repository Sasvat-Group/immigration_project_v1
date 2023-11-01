import React, { useState } from 'react'
import { Card, Col, Nav, Row, Tab } from 'react-bootstrap'
import { v4 as uuidv4 } from 'uuid';
import './reports.style.scss';
import PageHeader from 'layouts/PageHeader/PageHeader';

const importLazyTabs = (component) => {
    return React.lazy(() => import("./TabComponents").then(module => ({ default: module[component] })))
}

const OperationalReports = importLazyTabs('OperationalReports');
const ComplianceReports = importLazyTabs('ComplianceReports');
const PerformanceMetricsReport = importLazyTabs('PerformanceMetricsReport');

export default function Reports() {
    const user_type = localStorage.getItem('user_type')
    let user_type_tabs = [{
        title: 'Operational Reports',
        component: <OperationalReports user_type={user_type} />,
        active: true
    }, {
        title: 'Compliance Reports',
        component: <ComplianceReports user_type={user_type}/>,
        active: false
    }, {
        title: 'Performance Metrics Report',
        component: <PerformanceMetricsReport user_type={user_type}/>,
        active: false
    }]

    if (user_type === 'hr') {
        user_type_tabs = [{
            title: 'Operational Reports',
            component: <OperationalReports user_type={user_type}/>,
            active: true
        }, {
            title: 'Compliance Reports',
            component: <ComplianceReports user_type={user_type}/>,
            active: false
        }]
    }

    const [tabs, setTabs] = useState(user_type_tabs)

    const handleTabClick = (index) => {

        let nTabs = tabs.map(tab => {
            tab.active = false
            return tab;
        })

        nTabs[index].active = true;
        setTabs(nTabs)
    }

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Reports" BreadcrumbItemList={[{ name: 'Reports' }]} />

            <Row>
                <Col lg={4}>
                    <Card className="custom-card">
                        <Card.Body className='ht-450'>
                            <h4 className='main-content-label mb-3'>Power BI Dashboard</h4>
                            <div className="embed-responsive embed-responsive-4by3">
                                <iframe title="Immigration Online Dashboard  - Home"
                                    width="600"
                                    height="373.5"
                                    src="https://app.powerbi.com/view?r=eyJrIjoiMmE3NjFlMzEtODM3NS00MDZhLTgxN2MtYzQ1ZmNiNjc5MmFkIiwidCI6ImU4NDUyOGM1LTRkODYtNDkzNC05YmUwLWE2YjM2MjJjZjEwNyIsImMiOjF9"
                                    frameBorder="0"
                                    allowFullScreen={true}>
                                </iframe>
                            </div>
                        </Card.Body>
                    </Card>
                </Col>
                <Col lg={8} className="beneficiary-info-container">
                    <Card>
                        <Card.Body className='ht-450'>
                            <h4 className='main-content-label mb-3'>Report Info</h4>
                            <Tab.Container id="left-tabs-example" defaultActiveKey="first">
                                <Row>
                                    <Col lg={3}>
                                        <Nav variant="pills" className="flex-column">
                                            {tabs.map((tab, index) => {
                                                return (<Nav.Item key={uuidv4()}>
                                                    <Nav.Link active={tab.active === true} onClick={() => handleTabClick(index)} eventKey={index}>{tab.title}</Nav.Link>
                                                </Nav.Item>);
                                            })}
                                        </Nav>
                                    </Col>
                                    <Col lg={9}>
                                        <Tab.Content className='tab-content'>
                                            <React.Suspense fallback={<h2>Loading</h2>}>
                                                {tabs.map((tab, index) => {
                                                    return <Tab.Pane key={uuidv4()} eventKey={index} active={tab.active === true}>
                                                        {tab.active === true ? tab.component : <h2>not active</h2>}
                                                    </Tab.Pane>
                                                })}
                                            </React.Suspense>
                                        </Tab.Content>
                                    </Col>
                                </Row>
                            </Tab.Container>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </React.Fragment>
    )
}

