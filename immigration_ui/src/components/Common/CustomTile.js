import React from 'react'
import { Badge, Card } from "react-bootstrap"
import { v4 as uuid } from 'uuid'
import './CustomTile.scss'

const CustomTile = ({ initialState }) => {

    if (!initialState)
        return null

    const TileData = ({ values, type }) => {

        return values.map((value) => {

            return type === 'label' ? <h5 key={uuid()} className="tile-label">{value}</h5> : <h3 key={uuid()} className="badge-mark"><Badge bg="dark">{value}</Badge></h3>
        })
    }

    return (
        <Card className="custom-card">
            <Card.Body>
                <div className="card-item">
                    <div className="custom-tile">

                        {initialState.columns.map(column => {

                            return <div className="tile-content bg-transparent" key={uuid()}>
                                <h5 className="main-content-label">{column.title}</h5>
                                <span className="tile-description">
                                    {column.description !== undefined ? column.description : ''}
                                </span>
                                <div className="tile-body">
                                    <div className="labels">
                                        <TileData type='label' values={column.labels} />
                                    </div>
                                    <div className="values">
                                        <TileData type='value' values={column.values} />
                                    </div>
                                </div>
                            </div>

                        })}

                    </div>
                </div>
            </Card.Body>
        </Card>
    )
}

export default CustomTile