import React from "react";
import { useEffect } from "react";
import { useState } from "react";

// https://reactjs.org/docs/hooks-overview.html
// Hooks are functions that let you “hook into” React state and lifecycle features from function components, instead of classes.
// Basically waits to run logic on a user's input for a certain amount of time to prevent performing logic before the user is done typing their input.
// For example: I want to type youtube. I type "y", then the program performs logic, I type "o", then the program performs more logic, etc. 
// With debouncer, it waits a certain amount of time for me to stop inputting (including deleting). youtbe -> youtube -> pause, perform logic

export function useDebounce(value, timeout, callback) {
  const [timer, setTimer] = useState(null);

  const clearTimer = () => {
    if (timer) clearTimeout(timer);
  };

  useEffect(() => {
    clearTimer();

    if (value && callback) {
      const newTimer = setTimeout(callback, timeout);
      setTimer(newTimer);
    }
  }, [value]);
}