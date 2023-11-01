import React, { useState } from "react";

import DatePicker from "react-datepicker";

export const Datepicker = () => {
    const [startDate, setStartDate] = useState(new Date());
    return (
      <DatePicker
        className="form-control"
        selected={startDate}
        onChange={(date) => setStartDate(date)}
      />
    );
  };