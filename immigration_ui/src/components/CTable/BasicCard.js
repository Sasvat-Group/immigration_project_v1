import React, { Fragment } from "react"
import { Card, ListGroup } from 'react-bootstrap'
import { v4 as uuid } from 'uuid'

export function Basiccard(props) {

  const listItems = Object.keys(props.data).map(key => {
    return (
      <li key={uuid()} className='d-flex justify-content-between'>
        <span>{props.data[key]["displayName"]}</span>
        <b>{props.data[key]["value"].toString()}</b></li>
    )
  })

  const data = [{
    name: 'Project Specific Supporting Documents', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2F2883%2DI%2D485%20Application&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
  }, {
    name: 'Government Filings', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Filings&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
  }, {
    name: 'Government Notices', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Notices&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
  }, {
    name: 'Receipt Notice', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Notices%2F2021%2DMar%5FI%2D485%5FAOS%20Receipt%20Notice%5FIMMICorp1%5FMartin%2C%20John%2Epdf&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf&parent=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Notices`
  }, {
    name: 'Approval Notice', link: ``
  }, {
    name: 'Filing Copy', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Filings%2F2022%2DJan%5FI%2D485%5FAOS%2DEAD%2DAP%20Filing%2C%20IMMICorp1%5FMARTIN%2C%20John%2Epdf&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf&parent=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2FGovernment%20Filings`
  }, {
    name: 'Project ID and Project Name: 2883-I-485 Application', link: `https://immilytics.sharepoint.com/sites/1310-JohnMartin/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2F1310%2DJohnMartin%2FShared%20Documents%2FDocument%20Library%2F2883%2DI%2D485%20Application&viewid=130cda98%2Dcf06%2D44c8%2D9527%2D4dc0985264bf`
  }]

  const handleLink = (link) => {
    window.open(link, '_blank')
  }

  return (
    <Fragment>
      <Card className="custom-card border-left">
        <Card.Body className="case-specific-overview">
          <h5 className="main-content-label">{props.cardName}</h5>
          <ul className="lh-lg mt-4">{listItems}</ul>

          <h5 className="main-content-label">Document Links</h5>
          <ListGroup className="projects-list mt-1" >
            {data.map((item, index) => {
              return <ListGroup.Item action
                className="flex-column align-items-start p-2"
                key={index}
              >
                <div onClick={() => handleLink(item.link)} className="d-flex w-100 justify-content-between">
                  <h6 className="mb-1 font-weight-semibold ">{item.name}</h6>
                </div>
              </ListGroup.Item>
            })}
          </ListGroup>
        </Card.Body>
      </Card>
    </Fragment >
  )
}