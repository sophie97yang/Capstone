import React, { useState, useEffect, useRef } from "react";
import {useHistory} from 'react-router-dom';
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import DeleteModal from "./DeleteModal";

function TripOptions({trip}) {
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const history = useHistory();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current?.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const ulClassName = "trip-options" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
      <button onClick={openMenu}>
        <i className="fa-solid fa-ellipsis"/>
      </button>
      <ul className={ulClassName} ref={ulRef}>
        <li>
          <i className="fa-solid fa-user-plus"/>
            <OpenModalButton
              buttonText="Invite Others"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />
          </li>
          <li>
          <i className="fa-solid fa-trash-can"/>
            <OpenModalButton
              buttonText="Delete"
              onItemClick={closeMenu}
              modalComponent={<DeleteModal trip={trip} />}
            />
          </li>
      </ul>
    </>
  );
}

export default TripOptions;
