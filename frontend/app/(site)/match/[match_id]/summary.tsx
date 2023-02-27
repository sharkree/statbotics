import React from "react";

import { classnames } from "../../../../utils";
import { Data } from "./types";

const Summary = ({ data }: { data: Data }) => {
  const winProb = data.match.epa_win_prob;
  const redWinProb = winProb * 100;
  const blueWinProb = (1 - winProb) * 100;

  const redPred = data.match.red_epa_pred * (1 + data.year.foul_rate);
  const bluePred = data.match.blue_epa_pred * (1 + data.year.foul_rate);

  const redScore = data.match.red_score;
  const blueScore = data.match.blue_score;

  const completed = data.match.status === "Completed";

  return (
    <div className="w-full flex flex-col items-center">
      <p className="text-3xl lg:text-3xl mt-8 mb-4">Summary</p>
      <div className="w-full flex flex-col md:flex-row justify-center gap-4 md:gap-16">
        <div className="flex flex-col items-center">
          <div className="flex text-3xl">
            <p className={classnames("data text-red-500", redPred > bluePred ? "font-bold" : "")}>
              {Math.round(redPred)}
            </p>
            <p className="mx-2">-</p>
            <p className={classnames("data text-blue-500", bluePred > redPred ? "font-bold" : "")}>
              {Math.round(bluePred)}
            </p>
          </div>
          <div className="mt-4 text-lg flex">
            Projected Winner:{" "}
            <p
              className={classnames(
                "ml-2",
                data.match.pred_winner === "red" ? "text-red-500" : "text-blue-500"
              )}
            >
              {data.match.pred_winner.toUpperCase()}
            </p>
          </div>
        </div>
        <div className="h-full w-1 bg-gray-300" />
        <div className="flex flex-col items-center">
          <div className="flex text-3xl">
            {redWinProb > blueWinProb ? (
              <p className="data text-red-500">{Math.round(redWinProb)}%</p>
            ) : (
              <p className="data text-blue-500">{Math.round(blueWinProb)}%</p>
            )}
          </div>
          <div className="mt-4 text-lg flex">Win Probability</div>
        </div>
        <div className="h-full w-1 bg-gray-300" />
        <div className="flex flex-col items-center">
          <div className="flex text-3xl">
            <p className={classnames("data text-red-500", redScore > blueScore ? "font-bold" : "")}>
              {completed ? Math.round(redScore) : ""}
            </p>
            <p className="mx-2">-</p>
            <p
              className={classnames("data text-blue-500", blueScore > redScore ? "font-bold" : "")}
            >
              {completed ? Math.round(blueScore) : ""}
            </p>
          </div>
          <div className="mt-4 text-lg flex">
            Actual Winner:{" "}
            <p
              className={classnames(
                "ml-2",
                completed ? (data.match.winner === "red" ? "text-red-500" : "text-blue-500") : ""
              )}
            >
              {completed ? data.match.winner.toUpperCase() : "N/A"}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Summary;
