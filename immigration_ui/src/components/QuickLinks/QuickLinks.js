import React from 'react'
import { Button, Card, Col, Row } from 'react-bootstrap'
import './quick-links.style.scss';
import PageHeader from 'layouts/PageHeader/PageHeader';

export default function QuickLinks() {

    const data = [{
        title: "USCIS",
        list: [{
            name: "Home",
            link: "https://www.uscis.gov/"
        }, {
            name: "Forms",
            link: "https://www.uscis.gov/forms/forms"
        }, {
            name: "Check your Project status",
            link: "https://egov.uscis.gov/casestatus/landing.do"
        }, {
            name: "Check Processing Times",
            link: "https://egov.uscis.gov/processing-times/"
        }, {
            name: "Address Change Form",
            link: "https://egov.uscis.gov/coa/displayCOAForm.do"
        }]
    }, {
        title: "CBP",
        list: [{
            name: "Most Recent I-94",
            link: "https://i94.cbp.dhs.gov/I94/#/home"
        }, {
            name: "View Travel History",
            link: "https://i94.cbp.dhs.gov/I94/#/home"
        }, {
            name: "Apply for New I-94",
            link: "https://i94.cbp.dhs.gov/I94/#/home"
        }]
    }, {
        title: "DOS (Department of State)",
        list: [{
            name: "Home",
            link: "https://travel.state.gov/content/travel.html"
        }, {
            name: "List of Embassies and Consulates",
            link: "https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/list-of-posts.html"
        }, {
            name: "Visa Appointment Wait Times",
            link: "https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/wait-times.html"
        }, {
            name: "Visa Bulletin",
            link: "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html"
        }, {
            name: "U.S. Visas",
            link: "https://travel.state.gov/content/travel/en/us-visas.html"
        }, {
            name: "U.S. Visas Reciprocity and Civil Documents By Country",
            link: "https://travel.state.gov/content/travel/en/us-visas/Visa-Reciprocity-and-Civil-Documents-by-Country.html"
        }]
    }, {
        title: "DOL (Department of Labor)",
        list: [{
            name: "FLC Data Center",
            link: "https://www.flcdatacenter.com/"
        }, {
            name: "FLAG System - Home",
            link: "https://secure.login.gov/?request_id=1187793d-6942-4ff7-b276-b6e0c9346cd2"
        }, {
            name: "FLAG System Portal",
            link: "https://flag.dol.gov/"
        }, {
            name: "PERM Website",
            link: "https://www.plc.doleta.gov/eta_start.cfm?actiontype=logout"
        }]
    }]

    return (
        <React.Fragment>
            {/* <!-- Page Header --> */}
            <PageHeader Header="Quick Links" BreadcrumbItemList={[{ name: 'Quick Links' }]} />

            <div className='quick-links-container'>
                <Row>
                    {data.map((item, index) => (
                        <Col xl={3}>
                            <Card className="custom-card">
                                <Card.Body>
                                    <h5 className="main-content-label">{item.title} <i className="fe fe-link"></i></h5>
                                    <div className="btn-list">
                                        {item.list.map((link) => (
                                            <Button variant={index % 2 === 0 ? "primary" : "secondary"} type="button">{link.name}</Button>
                                        ))}
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            </div>
        </React.Fragment>
    )
}
