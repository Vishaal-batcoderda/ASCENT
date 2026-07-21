import React from "react";
import GlassCard from "../ui/GlassCard";

function ReflectionCard({ reflection }) {

    if (!reflection) return null;

    return (
        <GlassCard>

            <h2 className="text-xl font-bold mb-4">
                Reflection Agent
            </h2>

            <div className="space-y-4">

                <div>
                    <p className="text-sm opacity-70">
                        Overall Quality
                    </p>

                    <p className="font-semibold">
                        {reflection.overall_quality}
                    </p>
                </div>

                <div>
                    <p className="text-sm opacity-70">
                        Confidence
                    </p>

                    <p>
                        {reflection.confidence}%
                    </p>
                </div>

                <div>
                    <p className="text-sm opacity-70">
                        Summary
                    </p>

                    <p>
                        {reflection.summary}
                    </p>
                </div>

                {reflection.strengths?.length > 0 && (
                    <div>

                        <p className="text-sm opacity-70 mb-2">
                            Strengths
                        </p>

                        <ul className="list-disc pl-6">

                            {reflection.strengths.map((item, i) => (
                                <li key={i}>{item}</li>
                            ))}

                        </ul>

                    </div>
                )}

                {reflection.weaknesses?.length > 0 && (
                    <div>

                        <p className="text-sm opacity-70 mb-2">
                            Weaknesses
                        </p>

                        <ul className="list-disc pl-6">

                            {reflection.weaknesses.map((item, i) => (
                                <li key={i}>{item}</li>
                            ))}

                        </ul>

                    </div>
                )}

            </div>

        </GlassCard>
    );
}

export default ReflectionCard;