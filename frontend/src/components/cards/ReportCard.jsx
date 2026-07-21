import ReactMarkdown from "react-markdown";
import GlassCard from "../ui/GlassCard";

function ReportCard({ report }) {

    return (

        <GlassCard>

            <h2 className="text-xl font-semibold mb-5">
                AI Investment Report
            </h2>

            {
                report ? (

                    <article
                        className="
                            prose
                            prose-invert
                            max-w-none

                            prose-headings:text-white
                            prose-headings:font-bold
                            prose-headings:tracking-tight

                            prose-h1:text-3xl
                            prose-h2:text-2xl
                            prose-h3:text-xl

                            prose-headings:mt-8
                            prose-headings:mb-4

                            prose-p:text-slate-300
                            prose-p:leading-8
                            prose-p:mb-4

                            prose-ul:my-4
                            prose-li:my-1
                            prose-li:text-slate-300

                            prose-strong:text-white
                        "
                    >

                        <ReactMarkdown>
                            {report}
                        </ReactMarkdown>

                    </article>

                ) : (

                    <p className="text-slate-500">
                        Analyze a stock to generate an AI report.
                    </p>

                )

            }

        </GlassCard>

    );

}

export default ReportCard;