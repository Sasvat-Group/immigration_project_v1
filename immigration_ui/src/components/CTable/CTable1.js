import React from 'react'
import Box from '@mui/material/Box'
import Collapse from '@mui/material/Collapse'
import IconButton from '@mui/material/IconButton'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown'
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp'
import { Row, Col } from 'react-bootstrap'
import { Basiccard } from './BasicCard'
import Milestone from "../Milestone"
import "./CTable.style.scss"

const caseOverview = [{
  CRN: { displayName: "Project Receipt Number", value: "MSC2290202202" },
  LSC: { displayName: "Last Step Completed", value: "Received Receipt Notice" },
  LSCD: { displayName: "Last Step Completed Date", value: "2021-09-21" },
  NSD: { displayName: "Next Step Due", value: "Received Decision Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2022-03-20 " }
}, {
  CRN: { displayName: "Project Receipt Number", value: "MSC2290202201" },
  LSC: { displayName: "Last Step Completed", value: "Received Receipt Notice" },
  LSCD: { displayName: "Last Step Completed Date", value: "2021-09-21" },
  NSD: { displayName: "Next Step Due", value: "Received Decision Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2022-03-20 " }
}
  ,
{
  CRN: { displayName: "Project Receipt Number", value: "MSC2290202200" },
  LSC: { displayName: "Last Step Completed", value: "Project Filed & Sent" },
  LSCD: { displayName: "Last Step Completed Date", value: "2021-10-02" },
  NSD: { displayName: "Next Step Due", value: "Received Receipt Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2021-10-09" }
}
  ,
{
  CRN: { displayName: "Project Receipt Number", value: "LIN2135551344" },
  LSC: { displayName: "Last Step Completed", value: "Project Filed & Sent" },
  LSCD: { displayName: "Last Step Completed Date", value: "2021-09-08" },
  NSD: { displayName: "Next Step Due", value: "Received Receipt Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2021-09-15" }
}
  , {
  CRN: { displayName: "Project Receipt Number", value: "SRC2119751089" },
  LSC: { displayName: "Last Step Completed", value: "Received Receipt Notice" },
  LSCD: { displayName: "Last Step Completed Date", value: "2001-03-26" },
  NSD: { displayName: "Next Step Due", value: "Received Decision Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2001-09-22" }
}
  , {
  CRN: { displayName: "Project Receipt Number", value: "A2024494140" },
  LSC: { displayName: "Last Step Completed", value: "Received Decision Notice" },
  LSCD: { displayName: "Last Step Completed Date", value: "2022-07-16" },
  NSD: { displayName: "Next Step Due", value: "Sent Decision Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2022-07-17" }
}
  , {
  CRN: { displayName: "Project Receipt Number", value: "EAC1814052631" },
  LSC: { displayName: "Last Step Completed", value: "Received Decision Notice" },
  LSCD: { displayName: "Last Step Completed Date", value: "2001-09-22" },
  NSD: { displayName: "Next Step Due", value: "Sent Decision Notice" },
  NSDD: { displayName: "Next Step Due Date", value: "2001-09-23" }
}
]

function createData(caseId, petitionName, openedDate, targetFileDate, filedDate, primaryStatus, secondaryStatus, approvedClosedDate, lcaETA, turnAroundTime) {
  return {
    caseId,
    petitionName,
    openedDate,
    targetFileDate,
    filedDate,
    primaryStatus,
    secondaryStatus,
    approvedClosedDate,
    lcaETA,
    turnAroundTime,
    history: [
      {
        date: '2020-01-05',
        customerId: '11091700',
        amount: 3,
      },
      {
        date: '2020-01-02',
        customerId: 'Anonymous',
        amount: 1,
      },
    ],
  }
}

function RowData(props) {
  const { row, index } = props
  const [open, setOpen] = React.useState(false)

  return (
    <React.Fragment>
      <TableRow>
        <TableCell>
          <IconButton
            aria-label="expand row"
            size="small"
            onClick={() => setOpen(!open)}
          >
            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
          </IconButton>
        </TableCell>
        <TableCell component="th" scope="row">{row.caseId}</TableCell>
        <TableCell align="right">{row.petitionName}</TableCell>
        <TableCell align="right">{row.openedDate}</TableCell>
        <TableCell align="right">{row.targetFileDate}</TableCell>
        <TableCell align="right">{row.filedDate}</TableCell>
        <TableCell align="right">{row.primaryStatus}</TableCell>
        <TableCell align="right">{row.secondaryStatus}</TableCell>
        <TableCell align="right">{row.approvedClosedDate}</TableCell>
        <TableCell align="right">{row.lcaETA ? <a href={row.lcaETA} rel="noreferrer" target="_blank">View</a> : null}</TableCell>
        <TableCell align="right">{row.turnAroundTime}</TableCell>
      </TableRow>
      <TableRow>
        <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={12}>
          <Collapse in={open} timeout="auto" unmountOnExit>
            <Box>
              <Row>
                <Col lg={3} className='case-specific-basic-card'>
                  <Basiccard key={row.caseId} cardName="Project Overview" data={caseOverview[index]}></Basiccard>
                </Col>
                <Col lg={9} className='case-specific-milestone-card'>
                  <Milestone row={row}></Milestone>
                </Col>
              </Row>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </React.Fragment>
  )
}

const rows = [
  createData('2881', 'I-765 Application', "2021-09-02", "2021-09-12", "2022-01-05", "Approved", "Decision Notice Received", "2022-05-04", "NA", "125"),
  createData('2882', 'I-131 Application', "2021-09-02", "2021-09-12", "2022-01-05", "Approved", "Decision Notice Received", "2022-05-04", "NA", "125"),
  createData('2883', 'I-485 Application', "2021-09-02", "2021-09-15", "2022-01-05", "Approved", "Received Biometrics Notice", "2022-05-04", "NA", "125"),
  createData('2884', 'I-140 Petition', "2021-08-31", "2021-09-07", "2021-09-24", "Open", "Decision Notice Received", "2021-09-29", "NA", "24"),
  createData('2885', 'H - 1B Petition', "2021-02-12", "2021-03-12", "2021-04-15", "Approved", "Decision Notice Received", "2021-05-07", "https://www.google.com", "62"),
  createData('2886', 'PERM Application', "2020-10-19", "2021-10-19", "2021-04-14", "Approved", "Decision Notice Received", "2021-08-30", "NA", "177"),
  createData('2887', 'H-1B Change of Status Bachelor\'s CAP', "2018-03-02", "2018-04-02", "2018-04-02", "Approved", "Decision Notice Received", "2018-05-07", "https://www.google.com", "31"),
]

export default function CollapsibleTable(props) {
  return (
    <TableContainer>
      <Table aria-label="collapsible table">
        <TableHead>
          <TableRow>
            <TableCell />
            <TableCell>Project ID</TableCell>
            <TableCell align="right">Petition Name</TableCell>
            <TableCell align="right">Opened Date</TableCell>
            <TableCell align="right">Target File Date</TableCell>
            <TableCell align="right">Filed Date</TableCell>
            <TableCell align="right">Primary<br />Status</TableCell>
            <TableCell align="right">Secondary<br />Status</TableCell>
            <TableCell align="right">Approved/<br />Closed Date</TableCell>
            <TableCell align="right">LCA/<br />ETA9089</TableCell>
            <TableCell align="right">Turnaround Time</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row, index) => (
            <RowData key={row.caseId} index={index} row={row} />
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  )
}